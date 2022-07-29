# Module `config.py`
> Path: `mds_lib\base\config.py`
## Class `RouteHandler`
### SubElement(s)
 > `__route_upload`: str = None
 > `__route_download`: str = None
 > `__route_delete`: str = None
 > `__route_list`: str = None
 > `__is_https`: Optional[bool] = None
 > ## Function  `route_upload`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_download`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_delete`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_list`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `is_https`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `Optional[bool]`
 > ## Function  `__init__`
 > ### Argument(s)
 > + `mds_host`: str - empty doc string
 > ## Function  `__parse_response`
 > ### Argument(s)
 > + `response`: requests.Response - empty doc string
## Class `Config`
### Decorator(s)
+ Singleton
### SubElement(s)
 > `__mds_access_token`: str = None
 > `__mds_host`: str = None
 > `__mds_router`: RouteHandler = None
 > `__mds_file_types_to_extract`: Optional[Union[List[str], Dict[str, str], str]] = None
 > `__mds_files_to_extract`: Optional[Union[List[str], Dict[str, str], str]] = None
 > `__mds_local_path`: Optional[str] = None
 > ## Function  `mds_access_token`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `mds_host`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `mds_file_types`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `Optional[Union[List[str], Dict[str, str], str]]`
 > ## Function  `mds_files`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `Optional[Union[List[str], Dict[str, str], str]]`
 > ## Function  `mds_local_path`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `Optional[str]`
 > ## Function  `route_upload`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_download`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_delete`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `route_list`
 > ### Decorator(s)
 > + property
 > #### Declared returns: `str`
 > ## Function  `__init__`
 > ## Function  `reload_configs`
 > ## Function  `__load_config_file`
 > ### Decorator(s)
 > + staticmethod
 > ### Argument(s)
 > + `file`: Path - empty doc string
 > #### Declared returns: `Dict[str, Any]`