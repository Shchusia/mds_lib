import time
from pathlib import Path

import pytest

from mds_lib import (
    command_get_list,
    command_init_config,
    command_pull_file,
    command_push_file,
    command_remove_file,
)
from mds_lib.exc import MDSConfigException, MDSRequestException
from tests.utils import (
    MDS_TEST_ACCESS_TOKEN,
    MDS_TEST_HOST,
    TEST_FILE_TYPE,
    TEST_TMP_FILE,
    remove_config,
    remove_file,
)


def test_commands():
    remove_config()
    remove_file(TEST_TMP_FILE)
    with pytest.raises(MDSConfigException):
        list_files = command_get_list()
    command_init_config(mds_host=MDS_TEST_HOST, mds_access_token=MDS_TEST_ACCESS_TOKEN)
    list_files = command_get_list()
    assert len(list_files) == 0

    command_push_file(
        __file__,
        TEST_FILE_TYPE,
    )
    list_files = command_get_list()
    assert len(list_files) == 1
    assert Path(TEST_TMP_FILE).exists() is False
    command_pull_file(file_local="tmp_test_file.py", file_type=TEST_FILE_TYPE)

    assert Path(TEST_TMP_FILE).exists() is True
    remove_file(TEST_TMP_FILE)
    command_remove_file(file_type=TEST_FILE_TYPE)
    list_files = command_get_list()
    assert len(list_files) == 0
    time.sleep(0.5)
    with pytest.raises(MDSRequestException):
        command_pull_file(file_local="tmp_test_file.py", file_type=TEST_FILE_TYPE)

    remove_file(TEST_TMP_FILE)
    remove_config()
