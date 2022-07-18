"""
Library for working with MiniDataStorage
"""

from .logic import (
    command_get_list,
    command_init_config,
    command_pull_file,
    command_push_file,
    command_remove_file,
)

__version__ = "0.0.1"
__all__ = [
    "command_push_file",
    "command_remove_file",
    "command_get_list",
    "command_pull_file",
    "command_init_config",
]
