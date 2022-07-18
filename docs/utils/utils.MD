# Module `utils.py`
> Path: `mds\utils\utils.py`
## Function  `get_version`
```text
Method for getting the version of the library from the init file
:requirements: version must be specified separately
:good: __version__ = '0.0.1'
:bad: __version__, __any_variable__ = '0.0.1', 'any_value'
```
        
### Return
```text
version lib
```
                    
#### Declared returns: `Optional[str]`
## Class `GroupWithCommandOptions`
```text
Allow application of options to group with multi command
```

### Basses(s)
+ click.Group
### SubElement(s)
 > ## Function  `add_command`
 > ### Argument(s)
 > + `cmd` - empty doc string
 > + `name` - empty doc string
 > ## Function  `build_command_invoke`
 > ### Argument(s)
 > + `original_invoke` - empty doc string
 > ### SubElement(s)
 > > ## Function  `command_invoke`
 > > ```text
 > > insert invocation of group function
 > > ```
 > >
 > > ### Argument(s)
 > > + `ctx` - empty doc string