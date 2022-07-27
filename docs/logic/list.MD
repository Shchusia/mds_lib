# Module `list.py`
```text
Module with GetList command
```

> Path: `mds_lib\logic\list.py`
`COMMAND` = "GetList"
## Function  `command_get_list`
```text
Get existing list of files on remote storage
```
        
### Argument(s)
+ `file_type`: Optional[str] - get list concrete files
+ `is_view`: Optional[bool] - is view to console result default: False
### Return
```text
list of files information matching the condition `file_type`
```
                    
#### Declared returns: `List[ModelFile]`