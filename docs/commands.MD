# Module `commands.py`
> Path: `mds\commands.py`
## Function  `entry_point`
### Decorator(s)
+ click.group(help='Utility for work with mini data storage', cls=GroupWithCommandOptions, context_settings=dict(ignore_unknown_options=True))
+ click.option('-v', '--version', 'version', is_flag=True, required=False, default=False, help='Get library version', type=bool)
### Argument(s)
+ `version` - empty doc string
## Function  `init_config`
### Decorator(s)
+ entry_point.command('init', help='To init config file in order to work with mds.', context_settings=dict(ignore_unknown_options=True))
+ click.option('-o', '--overwrite', 'overwrite', is_flag=True, required=False, default=False, help='To overwrite, in case file already exists', type=bool)
### Argument(s)
+ `overwrite`: bool - empty doc string
## Function  `pull`
### Decorator(s)
+ entry_point.command('pull', help='Pull file from storage', context_settings=dict(ignore_unknown_options=True))
+ click.option('-f', '--file', 'file', required=False, help='File to upload', type=str)
+ click.option('-fl', '--file-local', 'file_local', required=False, help='File to save local', type=str)
+ click.option('-ft', '--file-type', 'file_type', required=False, default=None, help='file-type', type=str)
+ click.option('-o', '--overwrite', 'overwrite', is_flag=True, required=False, default=False, help='To overwrite, in case file already exists', type=bool)
### Argument(s)
+ `file` - empty doc string
+ `file_type` - empty doc string
+ `overwrite` - empty doc string
+ `file_local` - empty doc string
## Function  `push`
### Decorator(s)
+ entry_point.command('push', help='Push files to storage', context_settings=dict(ignore_unknown_options=True))
+ click.option('-ft', '--file-type', 'file_type', required=False, default=None, help='file-type', type=str)
+ click.option('-o', '--overwrite', 'overwrite', is_flag=True, required=False, default=False, help='To overwrite, in case file already exists', type=bool)
+ click.option('-f', '--file', 'file', required=True, help='File to upload', type=str)
### Argument(s)
+ `overwrite` - empty doc string
+ `file` - empty doc string
+ `file_type` - empty doc string
## Function  `remove`
### Decorator(s)
+ entry_point.command('remove', help='GetList existed files ')
+ click.option('-ft', '--file-type', 'file_type', required=False, default=None, help='file-type', type=str)
+ click.option('-f', '--file', 'file', required=False, help='File to upload', type=str)
### Argument(s)
+ `file` - empty doc string
+ `file_type` - empty doc string
## Function  `get_list`
### Decorator(s)
+ entry_point.command('list', help='GetList existed files ')
+ click.option('-ft', '--file-type', 'file_type', required=False, default=None, help='file-type', type=str)
### Argument(s)
+ `file_type`: str - empty doc string