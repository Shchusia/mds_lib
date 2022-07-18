"""
Setup MDS
"""
import os
import pathlib

from setuptools import setup

from mds_lib.utils.utils import get_version

LIB_NAME = "mds_lib"
HERE = pathlib.Path(__file__).parent


def get_packages():
    """
    Method get packages for apply into lib
    """
    ignore = ["__pycache__"]

    list_sub_folders_with_paths = [
        x[0].replace(os.sep, ".")
        for x in os.walk(LIB_NAME)
        if x[0].split(os.sep)[-1] not in ignore
    ]
    return list_sub_folders_with_paths


setup(
    name=LIB_NAME,
    version=get_version(),
    description="Library for work with MiniDataStorage",
    author="Denis Shchutkiy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="denisshchutskyi@gmail.com",
    # url="https://github.com/Shchusia/gendoc",
    packages=get_packages(),
    keywords=["pip", LIB_NAME],
    python_requires=">=3.7",
    entry_points={"console_scripts": [f"{LIB_NAME}={LIB_NAME}.commands:entry_point"]},
    install_requires=["click==8.1.2", "PyYAML==6.0", "requests==2.24.0"],
)
