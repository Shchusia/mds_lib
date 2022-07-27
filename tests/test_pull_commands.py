import os
from pathlib import Path
from typing import Dict, Optional

import pytest

from mds_lib import (
    command_pull_file_types,
    command_pull_files,
    command_push_file,
    command_remove_file,
)
from mds_lib.const import MDS_ACCESS_TOKEN_ENV_NAME, MDS_HOST_ENV_NAME
from mds_lib.exc import MDSRequestException
from tests.utils import (
    IS_PRINT,
    MDS_TEST_ACCESS_TOKEN,
    MDS_TEST_HOST,
    TEST_BASE_FOLDER,
    TEST_FILE_TYPE,
    TEST_FILE_TYPE_2,
    TEST_TMP_FILE,
    TEST_UTIL_FILE,
    TST_FLDR_1,
    TST_FLDR_2,
    TST_FLDR_3,
    get_just_name,
    remove_config,
    remove_file,
    remove_files_extracted_to_root_folder,
    remove_folder,
)


def validate_response(paths: Optional[Dict[str, Path]]):
    assert paths is not None
    for file_type, path in paths.items():
        if IS_PRINT:
            print(f"Type: {file_type}; Path: {path} ")
        assert path.is_file()


def test_pull_file_types():
    remove_config()
    remove_file(TEST_TMP_FILE)
    remove_folder(TEST_BASE_FOLDER)
    os.environ[MDS_HOST_ENV_NAME] = MDS_TEST_HOST
    os.environ[MDS_ACCESS_TOKEN_ENV_NAME] = MDS_TEST_ACCESS_TOKEN

    command_push_file(
        __file__,
        TEST_FILE_TYPE,
    )
    command_push_file(
        __file__,
        TEST_FILE_TYPE_2,
    )
    with pytest.raises(MDSRequestException):
        command_pull_file_types("test_file_type_unknown")

    validate_response(command_pull_file_types(TEST_FILE_TYPE_2))
    validate_response(command_pull_file_types(TEST_FILE_TYPE_2, local_path=TST_FLDR_1))
    validate_response(
        command_pull_file_types(
            [TEST_FILE_TYPE_2, TEST_FILE_TYPE], local_path=TST_FLDR_2
        )
    )
    validate_response(
        command_pull_file_types(
            {TEST_FILE_TYPE_2: "file_1.py", TEST_FILE_TYPE: "file_2.py"},
            local_path=TST_FLDR_3,
        )
    )
    command_remove_file(file_type=TEST_FILE_TYPE)
    command_remove_file(file_type=TEST_FILE_TYPE_2)
    #
    remove_folder(TEST_BASE_FOLDER)
    remove_files_extracted_to_root_folder()


def test_pull_files():
    remove_config()
    remove_file(TEST_TMP_FILE)
    remove_folder(TEST_BASE_FOLDER)
    os.environ[MDS_HOST_ENV_NAME] = MDS_TEST_HOST
    os.environ[MDS_ACCESS_TOKEN_ENV_NAME] = MDS_TEST_ACCESS_TOKEN

    command_push_file(
        __file__,
        TEST_FILE_TYPE,
    )
    command_push_file(
        TEST_UTIL_FILE,
        TEST_FILE_TYPE_2,
    )
    with pytest.raises(MDSRequestException):
        command_pull_files("test_pull_commands_unknown.py")
    file_name = get_just_name(__file__)
    utils_file_name = get_just_name(TEST_UTIL_FILE)
    validate_response(command_pull_files(file_name, local_path=TST_FLDR_1))
    validate_response(
        command_pull_files([utils_file_name, file_name], local_path=TST_FLDR_2)
    )
    validate_response(
        command_pull_files(
            {utils_file_name: "file_1.py", file_name: "file_2.py"},
            local_path=TST_FLDR_3,
        )
    )
    command_remove_file(file=file_name)
    command_remove_file(file=utils_file_name)
    remove_folder(TEST_BASE_FOLDER)
    remove_files_extracted_to_root_folder()
