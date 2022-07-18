"""
utils for logic functions
"""
import requests  # type: ignore

from mds.const import LOGGER


def handle_error(response: requests.Response) -> str:
    """Method converts error to pretty format if can"""
    try:
        data = response.json()["data"]
        resp = f""" {data['title']}
Detail: {data['detail']}
"""
    except Exception as exc:  # noqa
        LOGGER.debug(
            "Error in time convert error response. Error %s ", str(exc), exc_info=True
        )
        resp = response.text
    return resp
