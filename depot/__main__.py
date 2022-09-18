import argparse
import os
import sys

from pathlib import Path

from . import globals as g
from .utils.path import get_schema_path, join_paths


# TODO: refactor factor into separate module
def init(path: Path) -> None:
    data_dir_path = Path(join_paths(path, g.DATA_DIR_NAME))
    if data_dir_path.exists():
        print(
            f'Error: {data_dir_path} already exists as a file or directory',
            file=sys.stderr,
        )
        # TODO: error codes?
        sys.exit(1)

    os.environ[g.DATA_DIR_ENV_VAR] = str(data_dir_path)

    # TODO: fill directory
    os.mkdir(data_dir_path)
    os.mkdir(g.get_schemata_path())
    os.mkdir(get_schema_path(g.DEPOT_CATALOG_OID))
    os.mkdir(get_schema_path(g.INFORMATION_SCHEMA_OID))


parser = argparse.ArgumentParser(prog='depot')
subparsers = parser.add_subparsers(dest='command')

init_parser = subparsers.add_parser('init')
init_parser.add_argument(
    '-p',
    '--path',
    required=False,
    type=Path,
    default=Path.home(),
)


if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    if args.command == 'init':
        init(args.path)
