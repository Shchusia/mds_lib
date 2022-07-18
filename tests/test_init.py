from pathlib import Path

from mds_lib import command_init_config
from mds_lib.const import MDS_FILE_ENV_DEFAULT_VALUE
from tests.utils import MDS_TEST_ACCESS_TOKEN, MDS_TEST_HOST, remove_config


def test_init_command():
    """
    Test init logic command
    """
    remove_config()
    assert Path(MDS_FILE_ENV_DEFAULT_VALUE).exists() is False
    command_init_config(mds_host=MDS_TEST_HOST, mds_access_token=MDS_TEST_ACCESS_TOKEN)
    assert Path(MDS_FILE_ENV_DEFAULT_VALUE).exists() is True
    remove_config()
