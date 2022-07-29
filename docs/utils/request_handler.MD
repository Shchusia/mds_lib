# Module `request_handler.py`
> Path: `mds_lib\utils\request_handler.py`
## Class `AllowedMethods`
### Basses(s)
+ Enum
### SubElement(s)
 > `get` = "GET"
 > `post` = "POST"
 > `put` = "PUT"
 > `delete` = "DELETE"
`allowed_methods` = [method.value for method in AllowedMethods]
## Class `RequestHandler`
### Decorator(s)
+ Singleton
### SubElement(s)
 > ## Function  `__init__`
 > ## Function  `make_request`
 > ### Argument(s)
 > + `method`: str - empty doc string
 > + `url`: str - empty doc string
 > + `params`: Dict[str, Any] - empty doc string
 > + `data`: Dict[str, Any] - empty doc string
 > + `_json`: Dict[str, Any] - empty doc string
 > + `headers` - empty doc string
 > + `verify`: bool - empty doc string
 > + `files`: Dict[str, Any] - empty doc string
 > #### Declared returns: `requests.Response`