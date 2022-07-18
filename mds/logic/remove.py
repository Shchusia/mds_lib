"""
Module with remove command
"""
from typing import Optional

from mds.base.config import Config
from mds.const import LOGGER
from mds.exc import MDSRequestException
from mds.models.api_models import ModelFile
from mds.utils.request_handler import RequestHandler

from .utils import handle_error

COMMAND = "RemoveFile"


def command_remove_file(
    file: Optional[str] = None, file_type: Optional[str] = None
) -> ModelFile:
    """
    Remove file on remote system
    :param file: file name
    :param file_type: file type
    :return:
    """
    LOGGER.info(f"Started execution command: {COMMAND}")

    config = Config()
    params = dict(accessToken=config.mds_access_token)
    if file_type:
        params["fileType"] = file_type
    if file:
        params["fileName"] = file

    res = RequestHandler().make_request(
        "delete", url=config.route_delete, params=params
    )
    if res.status_code != 200:
        raise MDSRequestException(COMMAND, handle_error(res))
    data = res.json()
    LOGGER.info(f"Finished execution command: {COMMAND}")

    return ModelFile(**data["data"])
