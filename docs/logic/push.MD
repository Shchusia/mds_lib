# Module `push.py`
```text
Module with Push command
```

> Path: `mds_lib\logic\push.py`
`COMMAND` = "Push"
## Function  `command_push_file`
```text
Push file to remote storage
```
        
### Argument(s)
+ `file`: str - path to file in local system
+ `file_type`: Optional[str] - type file for separate file by logical types
+ `overwrite`: bool - overwrite if file with version
(if in name  provided version) exist on remote storage