from enum import Enum
from typing import Any, Dict

import requests  # type: ignore

from mds_lib.const import LOGGER
from mds_lib.exc import NotAllowedMethods
from mds_lib.utils.singleton import Singleton


class AllowedMethods(Enum):
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"


allowed_methods = [method.value for method in AllowedMethods]


@Singleton
class RequestHandler:
    def __init__(self):
        self._session = requests.session()

    def make_request(
        self,
        method: str,
        url: str,
        params: Dict[str, Any] = None,
        data: Dict[str, Any] = None,
        _json: Dict[str, Any] = None,
        headers=None,
        verify: bool = None,
        files: Dict[str, Any] = None,
    ) -> requests.Response:

        if method.upper() not in allowed_methods:
            raise NotAllowedMethods(
                incorrect_method=method, allowed_methods=allowed_methods
            )
        try:
            LOGGER.debug("started make_request %s %s", method, url)
            response = self._session.request(
                method=method,
                url=url,
                params=params,
                headers=headers,
                data=data,
                json=_json,
                verify=verify,
                files=files,
            )
            LOGGER.debug("finished make_request %s %s", method, url)
            return response
        except (
            requests.exceptions.SSLError,
            requests.exceptions.ConnectionError,
        ) as exc:
            LOGGER.warning("Invalid request.")
            raise exc
        except Exception as exc:
            raise exc
