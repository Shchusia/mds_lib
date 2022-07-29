# Module `exc.py`
```text
Exceptions
```

> Path: `mds_lib\exc.py`
## Class `MDSException`
```text
Main Exception
```

### Basses(s)
+ Exception
## Class `MDSConfigException`
```text
Exception with config mds lib
```

### Basses(s)
+ MDSException
### SubElement(s)
 > ## Function  `__init__`
## Class `MDSHostException`
```text
In provided incorrect mds host
```

### Basses(s)
+ MDSException
### SubElement(s)
 > ## Function  `__init__`
 > ### Argument(s)
 > + `incorrect_host`: str - empty doc string
## Class `MDSRequestException`
```text
Errors with http requests
```

### Basses(s)
+ MDSException
### SubElement(s)
 > ## Function  `__init__`
 > ### Argument(s)
 > + `request_type` - empty doc string
 > + `bad_response`: str - empty doc string
## Class `NotAllowedMethods`
### Basses(s)
+ MDSException
### SubElement(s)
 > ## Function  `__init__`
 > ### Argument(s)
 > + `incorrect_method`: str - empty doc string
 > + `allowed_methods`: list[str] - empty doc string