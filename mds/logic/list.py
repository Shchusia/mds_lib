"""
Module with GetList command
"""
from typing import List, Optional

from mds.base.config import Config
from mds.const import LOGGER
from mds.exc import MDSRequestException
from mds.models.api_models import ModelFile
from mds.utils.request_handler import RequestHandler

from .utils import handle_error

COMMAND = "GetList"


def command_get_list(
    file_type: Optional[str] = None, is_view: Optional[bool] = False
) -> List[ModelFile]:
    """
    Get existing list of files on remote storage

    :param file_type: get list concrete files
    :type file_type: Optional[str]
    :param is_view: is view to console result default: False
    :type is_view: bool
    :return: list of files information matching the condition `file_type`
    :rtype: ModelFile
    """
    LOGGER.info(f"Started execution command: {COMMAND}")
    config = Config()
    params = dict(accessToken=config.mds_access_token)
    if file_type:
        params["fileType"] = file_type
    res = RequestHandler().make_request(
        method="get", url=config.route_list, params=params
    )
    if res.status_code != 200:
        raise MDSRequestException(COMMAND, handle_error(res))
    data = res.json()["data"]
    if not data["files"]:
        LOGGER.info("Empty list files!")
        return []
    result = []
    for file in data["files"]:
        if is_view:
            print(file)
        result.append(ModelFile(**file))
    LOGGER.info(f"Finished execution command: {COMMAND}")
    return result
