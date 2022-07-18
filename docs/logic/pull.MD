# Module `pull.py`
```text
Module with Pull command
```

> Path: `mds\logic\pull.py`
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