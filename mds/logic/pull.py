"""
Module with Pull command
"""
from pathlib import Path
from typing import Optional
from uuid import uuid4

from mds.base.config import Config
from mds.const import LOGGER, SIZE_CHUNK_DOWNLOAD_FILE
from mds.exc import MDSRequestException
from mds.utils.request_handler import RequestHandler

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

    if file_local:
        path_to_save = check_file_local(file_local)
    elif file:
        path_to_save = check_file_local(file)
    else:
        path_to_save = check_file_local(f"file_{get_name_tmp_file()}.tmp")
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
