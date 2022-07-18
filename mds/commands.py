from pathlib import Path

import click
import yaml  # type: ignore  # noqa

from mds.const import (
    MDS_CONFIG_FILE_MDS_ACCESS_TOKEN,
    MDS_CONFIG_FILE_MDS_HOST,
    MDS_FILE_ENV_DEFAULT_VALUE,
)
from mds.logic import (
    command_get_list,
    command_init_config,
    command_pull_file,
    command_push_file,
    command_remove_file,
)
from mds.utils.utils import GroupWithCommandOptions, get_version


@click.group(
    help="Utility for work with mini data storage",
    cls=GroupWithCommandOptions,
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-v",
    "--version",
    "version",
    is_flag=True,
    required=False,
    default=False,
    help="Get library version",
    type=bool,
)
def entry_point(
    version,
):
    if version:
        print("MDS version: ", get_version())
    # if init_var:
    #     ctx.invoke(init_config)


@entry_point.command(
    "init",
    help="To init config file in order to work with mds.",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-o",
    "--overwrite",
    "overwrite",
    is_flag=True,
    required=False,
    default=False,
    help="To overwrite, in case file already exists",
    type=bool,
)
def init_config(overwrite: bool):
    print("MDS create config")
    file = Path(MDS_FILE_ENV_DEFAULT_VALUE)
    if file.is_file() and not overwrite:
        print("Such file already exists. To replace use the command '-o'")
        return
    print(f"Input `{MDS_CONFIG_FILE_MDS_HOST}`")
    mds_host = input()
    print(f"Input `{MDS_CONFIG_FILE_MDS_ACCESS_TOKEN}`")
    mds_access_token = input()
    command_init_config(mds_host=mds_host, mds_access_token=mds_access_token)


@entry_point.command(
    "pull",
    help="Pull file from storage",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-f",
    "--file",
    "file",
    required=False,
    help="File to upload",
    type=str,
)
@click.option(
    "-fl",
    "--file-local",
    "file_local",
    required=False,
    help="File to save local",
    type=str,
)
@click.option(
    "-ft",
    "--file-type",
    "file_type",
    required=False,
    default=None,
    help="file-type",
    type=str,
)
@click.option(
    "-o",
    "--overwrite",
    "overwrite",
    is_flag=True,
    required=False,
    default=False,
    help="To overwrite, in case file already exists",
    type=bool,
)
def pull(file, file_type, overwrite, file_local):
    print(file, file_type, overwrite, file_local)
    command_pull_file(
        file=file, file_local=file_local, file_type=file_type, overwrite=overwrite
    )


@entry_point.command(
    "push",
    help="Push files to storage",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option(
    "-ft",
    "--file-type",
    "file_type",
    required=False,
    default=None,
    help="file-type",
    type=str,
)
@click.option(
    "-o",
    "--overwrite",
    "overwrite",
    is_flag=True,
    required=False,
    default=False,
    help="To overwrite, in case file already exists",
    type=bool,
)
@click.option(
    "-f",
    "--file",
    "file",
    required=True,
    help="File to upload",
    type=str,
)
def push(overwrite, file, file_type):
    command_push_file(file, file_type, overwrite)


@entry_point.command("remove", help="GetList existed files ")
@click.option(
    "-ft",
    "--file-type",
    "file_type",
    required=False,
    default=None,
    help="file-type",
    type=str,
)
@click.option(
    "-f",
    "--file",
    "file",
    required=False,
    help="File to upload",
    type=str,
)
def remove(file, file_type):
    command_remove_file(file=file, file_type=file_type)


@entry_point.command("list", help="GetList existed files ")
@click.option(
    "-ft",
    "--file-type",
    "file_type",
    required=False,
    default=None,
    help="file-type",
    type=str,
)
def get_list(file_type: str):
    command_get_list(file_type=file_type, is_view=True)


if __name__ == "__main__":
    entry_point()
