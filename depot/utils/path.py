import os
import typing as t

from pathlib import Path


def join_paths(*paths: t.Union[Path, str]):
    return Path(os.path.join(*paths))


def get_schema_path(oid: int):
    from ..globals import get_schemata_path

    return join_paths(get_schemata_path(), str(oid))
