"""
Module with Pull command
"""
from pathlib import Path
from typing import Dict, List, Optional, Union
from uuid import uuid4

from mds_lib.base.config import Config
from mds_lib.const import (
    LOGGER,
    SIZE_CHUNK_DOWNLOAD_FILE,
    TEMPLATE_FILE_TYPE_EXTRACTED_FILES,
    TEMPLATE_NAME_EXTRACTED_FILES,
)
from mds_lib.exc import MDSRequestException
from mds_lib.utils.request_handler import RequestHandler

from .utils import handle_error

COMMAND = "Pull"


def get_name_tmp_file() -> str:
    """
    Get name file for tmp files
    """
    return str(uuid4()).split("-")[0]


def command_pull_file(
    file: Optional[str] = None,
    file_local: Optional[str] = None,
    dest: Optional[Union[str, Path]] = None,
    file_type: Optional[str] = None,
    overwrite: Optional[bool] = False,
) -> Optional[Path]:
    """
    Pull file from the remote storage

    if only type is specified will retrieve the latest version of the file
    :param file: name file on remote storage.
     can provide version in name file for extraction concreted version file.
     for get version use method list
    :type file: str
    :param file_local: with what name to save remote file to local
    :param file_type: additional condition for downloading
    :param overwrite: use True to overwrite if `file_local` exist in local storage.
    :type overwrite: bool
    :return:
    :example:
    >>> # on storage exist 3 files
    >>> # [{file: example_file.tst, file_type: 'test_type', version:0.0.1},  # num: 1
    >>> #  {file: example_file.tst, file_type: None, version:0.0.2},  # num: 2
    >>> #  {file: example_file.tst, file_type: None, version:0.0.3},]  # num: 3
    >>> command_pull_file(file='example_file.tst')
    <<< return: num 3
    >>> command_pull_file(file='example_file.0.0.2.tst')
    <<< return num 2
    >>> command_pull_file(file_type='test_type')
    <<< return num 1
    """

    def check_file_local(_file) -> Optional[Path]:
        file_path = Path(_file)
        if file_path.is_file() and not overwrite:
            LOGGER.warning("File exist in local storage. Use -o ")
            return None
        return file_path

    if not dest:
        dest = "./"
    if isinstance(dest, str):
        dest = Path(dest)
    dest.mkdir(exist_ok=True, parents=True)

    if file_local:
        path_to_save = check_file_local(dest / file_local)
    elif file:
        path_to_save = check_file_local(dest / file)
    else:
        path_to_save = check_file_local(
            dest
            / f"{TEMPLATE_NAME_EXTRACTED_FILES}{get_name_tmp_file()}{TEMPLATE_FILE_TYPE_EXTRACTED_FILES}"
        )
    if not path_to_save:
        return None
    config = Config()
    params = dict(accessToken=config.mds_access_token)
    if file_type:
        params["fileType"] = file_type
    if file:
        params["fileName"] = file

    res = RequestHandler().make_request("get", url=config.route_download, params=params)
    if res.status_code != 200:
        raise MDSRequestException("PullFile", handle_error(res))
    with open(path_to_save, "wb") as f:
        for chunk in res.iter_content(SIZE_CHUNK_DOWNLOAD_FILE):
            f.write(chunk)
    LOGGER.info("File saved. PathToFile %s", str(path_to_save))
    LOGGER.info(f"Finished execution command: {COMMAND}")
    return path_to_save


def command_pull_files(
    files_to_pull: Optional[Union[List[str], Dict[str, str], str]] = None,
    local_path: Optional[str] = None,
    overwrite: Optional[bool] = False,
) -> Optional[Dict[str, Path]]:
    """
    Pull many files by names

    Method for extraction many files.
    If the list is not provided, then it is taken from the config file
    from key `mds_pull_files`

    :param files_to_pull: files to pull
     can work with [str, list, dict]:
     str: extract one file
     list: list files to extract
     dict: dict files to extract {name_to_extract: local_name_path}
    :type files_to_pull: Union[List[str], Dict[str, str], str]
    :param local_path:
    :type local_path: Optional[str]
    :param overwrite: overwrite if file exist on local
    :type overwrite: bool
    :return: dict name to extract and local paths
    :rtype: Dict[str, Path]
    """
    config = Config()

    if not files_to_pull:
        if config.mds_files:
            files_to_pull = config.mds_files
            if not local_path and config.mds_local_path:
                local_path = config.mds_local_path
        else:
            LOGGER.info("No data for extraction")
            return None

    path_to_save = Path("./")
    if local_path:
        path_to_save = Path(local_path)
        path_to_save.mkdir(exist_ok=True, parents=True)

    result_dict = dict()  # type: Dict[str,Path]
    if isinstance(files_to_pull, str):
        result_dict[files_to_pull] = command_pull_file(
            file=files_to_pull, dest=path_to_save, overwrite=overwrite
        )
    elif isinstance(files_to_pull, list):
        for file in files_to_pull:
            result_dict[file] = command_pull_file(
                file=file, dest=path_to_save, overwrite=overwrite
            )
    elif isinstance(files_to_pull, dict):
        for file, local_path in files_to_pull.items():
            result_dict[file] = command_pull_file(
                file=file, file_local=local_path, dest=path_to_save, overwrite=overwrite
            )
    else:
        LOGGER.warning("Incorrect type for extraction files")
        return None
    return result_dict


def command_pull_file_types(
    file_types_to_pull: Optional[Union[List[str], Dict[str, str], str]] = None,
    local_path: Optional[str] = None,
    overwrite: Optional[bool] = False,
) -> Optional[Dict[str, Path]]:
    """

    :param file_types_to_pull:
    :param local_path:
    :param overwrite:
    :return:
    """
    config = Config()

    if not file_types_to_pull:
        if config.mds_file_types:
            file_types_to_pull = config.mds_file_types
            if not local_path and config.mds_local_path:
                local_path = config.mds_local_path
        else:
            LOGGER.info("No data for extraction")
            return None
    path_to_save = Path("./")
    if local_path:
        path_to_save = Path(local_path)
        path_to_save.mkdir(exist_ok=True, parents=True)

    result_dict = dict()  # type: Dict[str,Path]
    if isinstance(file_types_to_pull, str):
        result_dict[file_types_to_pull] = command_pull_file(
            file_type=file_types_to_pull, dest=path_to_save, overwrite=overwrite
        )
    elif isinstance(file_types_to_pull, list):
        for file_type in file_types_to_pull:
            result_dict[file_type] = command_pull_file(
                file_type=file_type, dest=path_to_save, overwrite=overwrite
            )
    elif isinstance(file_types_to_pull, dict):
        for file_type, local_path in file_types_to_pull.items():
            result_dict[file_type] = command_pull_file(
                file_type=file_type,
                file_local=local_path,
                dest=path_to_save,
                overwrite=overwrite,
            )
    else:
        LOGGER.warning("Incorrect type for extraction file_types")
        return None

    return result_dict
