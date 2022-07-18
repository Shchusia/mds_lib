"""
Module with init command
"""
import yaml  # type: ignore  # noqa

from mds.const import (
    LOGGER,
    MDS_CONFIG_FILE_MDS_ACCESS_TOKEN,
    MDS_CONFIG_FILE_MDS_HOST,
    MDS_FILE_ENV_DEFAULT_VALUE,
    MDS_SECTION_ENV_DEFAULT_VALUE,
)

COMMAND = "InitConfig"


def command_init_config(mds_host: str, mds_access_token: str):
    """Init mds config as file
    :param mds_host:  host where running MDS service
    :type mds_host: str
    :param mds_access_token: token which provided admin MDS service for your application
    :type mds_access_token: str
    :return: create file config in system. File name "./mds_config.yaml"
    """
    LOGGER.info(f"Started execution command: {COMMAND}")

    config = {
        MDS_SECTION_ENV_DEFAULT_VALUE: {
            MDS_CONFIG_FILE_MDS_HOST: mds_host,
            MDS_CONFIG_FILE_MDS_ACCESS_TOKEN: mds_access_token,
        }
    }
    with open(MDS_FILE_ENV_DEFAULT_VALUE, "w") as outfile:
        yaml.dump(config, outfile, default_flow_style=False)
    LOGGER.info(f"Finished execution command: {COMMAND}")
