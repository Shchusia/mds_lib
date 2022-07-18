import os

from mds.const import MDS_FILE_ENV_DEFAULT_VALUE

MDS_TEST_HOST = "http://localhost:8000"
MDS_TEST_ACCESS_TOKEN = "30bea63f-321e-488e-a136-3144a1cd4d43"
TEST_TMP_FILE = "tmp_test_file.py"
TEST_FILE_TYPE = "test_file"


def remove_file(file_path: str):
    try:
        os.remove(file_path)
    except:  # noqa
        print("Not existing config for remove")


def remove_config():
    remove_file(MDS_FILE_ENV_DEFAULT_VALUE)
