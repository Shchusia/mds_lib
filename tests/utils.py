import os
import shutil
from pathlib import Path
from typing import Union

from mds_lib.const import MDS_FILE_ENV_DEFAULT_VALUE, TEMPLATE_NAME_EXTRACTED_FILES

MDS_TEST_HOST = "http://localhost:8000"
MDS_TEST_ACCESS_TOKEN = "30bea63f-321e-488e-a136-3144a1cd4d43"
TEST_TMP_FILE = "tmp_test_file.py"
TEST_UTIL_FILE = __file__
TEST_FILE_TYPE = "test_file"
TEST_FILE_TYPE_2 = "test_file_2"

TEST_BASE_FOLDER = Path("test")

TST_FLDR_1 = TEST_BASE_FOLDER / "folder_1"
TST_FLDR_2 = TEST_BASE_FOLDER / "folder_2"
TST_FLDR_3 = TEST_BASE_FOLDER / "folder_3"
IS_PRINT = True


def remove_file(file_path: str):
    try:
        os.remove(file_path)
    except:  # noqa
        print("Not existing file for remove")


def remove_config():
    remove_file(MDS_FILE_ENV_DEFAULT_VALUE)


def remove_folder(path_to_folder: Union[str, Path] = TEST_BASE_FOLDER):
    try:
        shutil.rmtree(path_to_folder)
    except:  # noqa
        pass


def remove_files_extracted_to_root_folder():
    def is_file_to_remove(file_name: str):
        return len(file_name.split(TEMPLATE_NAME_EXTRACTED_FILES)) == 2

    path_to_folder = Path(__file__).absolute().parent
    print(path_to_folder)

    files = []
    for (dirpath, dirnames, filenames) in os.walk(path_to_folder):
        files.extend(filenames)
        break
    for file in files:
        if is_file_to_remove(file):
            remove_file(path_to_folder / file)


def get_just_name(path_to_file: str) -> str:
    return str(path_to_file).split(os.sep)[-1]
