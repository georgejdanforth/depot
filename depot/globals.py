import os

from functools import cache
from pathlib import Path

from .utils.path import join_paths

DATA_DIR_ENV_VAR = 'DEPOT_DATA_DIR'

DATA_DIR_NAME = '.depot'
SCHEMATA_DIR_NAME = 'schemata'


@cache
def get_data_dir_path() -> Path:
    if DATA_DIR_ENV_VAR in os.environ:
        data_dir_path = Path(os.environ[DATA_DIR_ENV_VAR])
    else:
        data_dir_path = Path(os.path.join(Path.home(), DATA_DIR_NAME))

    if not (data_dir_path.exists() and data_dir_path.is_dir()):
        raise RuntimeError(f'Data directory does not exist at {data_dir_path}')

    return data_dir_path


@cache
def get_schemata_path() -> Path:
    return join_paths(get_data_dir_path(), SCHEMATA_DIR_NAME)


DEPOT_CATALOG_OID = 0
INFORMATION_SCHEMA_OID = 1
