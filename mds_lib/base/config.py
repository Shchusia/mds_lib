import os
from pathlib import Path
from typing import Any, Dict, Optional

import requests  # type: ignore
import yaml  # type: ignore  # noqa

from mds_lib.const import (
    MDS_ACCESS_TOKEN_ENV_NAME,
    MDS_CONFIG_FILE_MDS_ACCESS_TOKEN,
    MDS_CONFIG_FILE_MDS_HOST,
    MDS_FILE_ENV_DEFAULT_VALUE,
    MDS_FILE_ENV_NAME,
    MDS_HOST_ENV_NAME,
    MDS_SECTION_ENV_DEFAULT_VALUE,
    MDS_SECTION_ENV_NAME,
)
from mds_lib.exc import MDSConfigException, MDSHostException, MDSRequestException
from mds_lib.utils.request_handler import RequestHandler
from mds_lib.utils.singleton import Singleton


class RouteHandler:
    __route_upload: str
    __route_download: str
    __route_delete: str
    __route_list: str
    __is_https: Optional[bool] = None

    @property
    def route_upload(self) -> str:
        return self.__route_upload

    @property
    def route_download(self) -> str:
        return self.__route_download

    @property
    def route_delete(self) -> str:
        return self.__route_delete

    @property
    def route_list(self) -> str:
        return self.__route_list

    @property
    def is_https(self) -> Optional[bool]:
        return self.__is_https

    def __init__(self, mds_host: str):
        parts = mds_host.split("://")
        response = None  # type: Optional[requests.Response ]
        if mds_host[-1] == "/":
            mds_host += "api"
        else:
            mds_host += "/api"
        if len(parts) == 1:
            try:
                try:
                    # try https
                    response = RequestHandler().make_request(
                        "get", "https://" + mds_host
                    )
                    self.__is_https = True
                except requests.exceptions.SSLError:
                    response = RequestHandler().make_request(
                        "get", "http://" + mds_host
                    )
                    self.__is_https = False
            except requests.exceptions.ConnectionError:
                raise MDSHostException(mds_host)
        else:
            response = RequestHandler().make_request("get", mds_host)
        if not response:
            raise ValueError(f"Not found handler for mds_host: `{mds_host}`")
        self.__parse_response(response)

    def __parse_response(self, response: requests.Response):
        if response.status_code == 200:
            data = response.json()["data"]
            self.__route_upload = data["uploadRoute"]
            self.__route_download = data["downloadRoute"]
            self.__route_delete = data["deleteRoute"]
            self.__route_list = data["listRoute"]

        else:
            data = ""
            try:
                data = str(response.json())
            except Exception:  # noqa
                data = response.text

            raise MDSRequestException("GetRoutes", data)


@Singleton
class Config:
    __mds_access_token: str
    __mds_host: str
    __mds_router: RouteHandler

    @property
    def mds_access_token(self) -> str:
        return self.__mds_access_token

    @property
    def mds_host(self) -> str:
        return self.__mds_host

    @property
    def route_upload(self) -> str:
        return self.mds_host + self.__mds_router.route_upload

    @property
    def route_download(self) -> str:
        return self.mds_host + self.__mds_router.route_download

    @property
    def route_delete(self) -> str:
        return self.mds_host + self.__mds_router.route_delete

    @property
    def route_list(self) -> str:
        return self.mds_host + self.__mds_router.route_list

    def __init__(self):
        self.reload_configs()

    def reload_configs(self):
        env_url = os.environ.get(MDS_HOST_ENV_NAME)
        env_token = os.environ.get(MDS_ACCESS_TOKEN_ENV_NAME)
        if env_url and env_token:
            self.__mds_host = env_url
            self.__mds_access_token = env_token
        else:
            path_file = Path(
                os.environ.get(MDS_FILE_ENV_NAME, MDS_FILE_ENV_DEFAULT_VALUE)
            )
            if not path_file.is_file():
                raise MDSConfigException()
            config = self.__load_config_file(path_file)
            section = os.environ.get(
                MDS_SECTION_ENV_NAME, MDS_SECTION_ENV_DEFAULT_VALUE
            )
            if section not in config:
                raise KeyError(f"Not section `{section}` in config file.")
            config_mds = config[section]
            if (
                MDS_CONFIG_FILE_MDS_HOST not in config_mds
                or MDS_CONFIG_FILE_MDS_ACCESS_TOKEN not in config_mds
            ):
                raise KeyError(
                    f"Section `{section}` must be contain required keys "
                    f"`{MDS_CONFIG_FILE_MDS_ACCESS_TOKEN}` "
                    f"& `{MDS_CONFIG_FILE_MDS_HOST}`"
                )
            self.__mds_host = config_mds[MDS_CONFIG_FILE_MDS_HOST]
            self.__mds_access_token = config_mds[MDS_CONFIG_FILE_MDS_ACCESS_TOKEN]
        self.__mds_router = RouteHandler(self.__mds_host)
        if self.__mds_host[-1] == "/":
            self.__mds_host = self.__mds_host[:-1]
        if self.__mds_router.is_https is not None:
            self.__mds_host = (
                "https://"
                if self.__mds_router.is_https
                else "http://" + self.__mds_host
            )

    @staticmethod
    def __load_config_file(file: Path) -> Dict[str, Any]:
        try:
            with open(file, "r") as f:
                config = yaml.safe_load(f)
            return config
        except Exception as exc:
            raise exc
