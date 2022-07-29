# Module `pull.py`
```text
Module with Pull command
```

> Path: `mds_lib\logic\pull.py`
`COMMAND` = "Pull"
## Function  `get_name_tmp_file`
```text
Get name file for tmp files
```
        
#### Declared returns: `str`
## Function  `command_pull_file`
```text
Pull file from the remote storage
if only type is specified will retrieve the latest version of the file
```
        
### Argument(s)
+ `file`: Optional[str] - name file on remote storage.
can provide version in name file for extraction concreted version file.
for get version use method list
+ `file_local`: Optional[str] - with what name to save remote file to local
+ `dest`: Optional[Union[str, Path]] - empty doc string
+ `file_type`: Optional[str] - additional condition for downloading
+ `overwrite`: Optional[bool] - use True to overwrite if `file_local` exist in local storage.
#### Declared returns: `Optional[Path]`
### Example 
```python
>>> # on storage exist 3 files
>>> # [{file: example_file.tst, file_type: 'test_type', version:0.0.1},  # num: 1
>>> #  {file: example_file.tst, file_type: None, version:0.0.2},  # num: 2
>>> #  {file: example_file.tst, file_type: None, version:0.0.3},]  # num: 3
>>> command_pull_file(file='example_file.tst')
<<< return: num 3
>>> command_pull_file(file='example_file.0.0.2.tst')
<<< return num 2
>>> command_pull_file(file_type='test_type')
<<< return num 1
```

### SubElement(s)
 > ## Function  `check_file_local`
 > ### Argument(s)
 > + `_file` - empty doc string
 > #### Declared returns: `Optional[Path]`
## Function  `command_pull_files`
```text
Pull many files by names
Method for extraction many files.
If the list is not provided, then it is taken from the config file
from key `mds_pull_files`
```
        
### Argument(s)
+ `files_to_pull`: Optional[Union[List[str], Dict[str, str], str]] - files to pull
can work with [str, list, dict]:
str: extract one file
list: list files to extract
dict: dict files to extract {name_to_extract: local_name_path}
+ `local_path`: Optional[str] - empty doc string
+ `overwrite`: Optional[bool] - overwrite if file exist on local
### Return
```text
dict name to extract and local paths
```
                    
#### Declared returns: `Optional[Dict[str, Path]]`
## Function  `command_pull_file_types`
```text
Pull many files by file_types
Method for extraction many files.
If the list is not provided, then it is taken from the config file
from key `mds_pull_file_types`
The same principle as with file_type like
```
        
### Argument(s)
+ `file_types_to_pull`: Optional[Union[List[str], Dict[str, str], str]] - file_types to pull
+ `local_path`: Optional[str] - path to folder to save
+ `overwrite`: Optional[bool] - is need overwrite if file exists   default: False
#### Declared returns: `Optional[Dict[str, Path]]`