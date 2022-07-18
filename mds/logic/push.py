"""
Module with Push command
"""
from pathlib import Path
from typing import Any, Dict, Optional

from mds.base.config import Config
from mds.const import LOGGER
from mds.exc import MDSRequestException
from mds.utils.request_handler import RequestHandler

from .utils import handle_error

COMMAND = "Push"


def command_push_file(
    file: str, file_type: Optional[str] = None, overwrite: bool = None
):
    """
    Push file to remote storage
    :param file:  path to file in local system
    :param file_type: type file for separate file by logical types
    :param overwrite: overwrite if file with version
     (if in name  provided version) exist on remote storage
    """
    LOGGER.info(f"Started execution command: {COMMAND}")
    file_path = Path(file)
    if not file_path.is_file():
        LOGGER.warning("File not found for upload")
        return
    config = Config()
    params = dict(accessToken=config.mds_access_token)  # type: Dict[str, Any]
    if file_type:
        params["fileType"] = file_type
    if overwrite:
        params["force"] = True
    res = RequestHandler().make_request(
        method="post",
        files={"file": open(file_path, "rb")},
        url=config.route_upload,
        params=params,
    )

    if res.status_code != 200:
        raise MDSRequestException(COMMAND, handle_error(res))
    LOGGER.info(f"Finished execution command: {COMMAND}")
