"""
Module with init command
"""
from pathlib import Path

import yaml  # type: ignore  # noqa

from mds_lib.const import (
    LOGGER,
    MDS_CONFIG_FILE_MDS_ACCESS_TOKEN,
    MDS_CONFIG_FILE_MDS_HOST,
    MDS_FILE_ENV_DEFAULT_VALUE,
)

COMMAND = "InitConfig"


def command_init_config(mds_host: str, mds_access_token: str, overwrite: bool = False):
    """Init mds config as file
    :param mds_host:  host where running MDS service
    :type mds_host: str
    :param mds_access_token: token which provided admin MDS service for your application
    :type mds_access_token: str
    :return: create file config in system. File name "./mds_config.yaml"
    """
    LOGGER.info(f"Started execution command: {COMMAND}")
    if Path(MDS_FILE_ENV_DEFAULT_VALUE).is_file() and not overwrite:
        LOGGER.info("Such file already exists. To replace use the command 'overwrite'")
        return None
    config_path = (
        Path(__file__).absolute().parent.parent / Path("src") / Path("template.yaml")
    )
    with open(
        config_path,
        "r",
    ) as file_src:
        with open(MDS_FILE_ENV_DEFAULT_VALUE, "w") as file_dist:
            data = file_src.read()
            print(data)
            data = data.replace(
                f'{MDS_CONFIG_FILE_MDS_HOST}: ""',
                f'{MDS_CONFIG_FILE_MDS_HOST}: "{mds_host}"',
            )
            data = data.replace(
                f'{MDS_CONFIG_FILE_MDS_ACCESS_TOKEN}: ""',
                f'{MDS_CONFIG_FILE_MDS_ACCESS_TOKEN}: "{mds_access_token}"',
            )
            file_dist.write(data)

    # with open(MDS_FILE_ENV_DEFAULT_VALUE, "w") as outfile:
    #     yaml.dump(config, outfile, default_flow_style=False)
    LOGGER.info(f"Finished execution command: {COMMAND}")
