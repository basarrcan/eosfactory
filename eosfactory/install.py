import os
#from termcolor import cprint, colored
import argparse
import pathlib

import eosfactory.core.utils as utils
import eosfactory.core.config as config


def tilde(tilde_path):
    return tilde_path.replace("~", str(pathlib.Path.home()))


def install(wsl_root=None):
    if wsl_root:
        map = config.config_map()
        map[config.wsl_root_[0]] = wsl_root
        config.write_config_map(map)
    
    current_path_color = "green"
    error_path_color = "red"

    while True:
        map = config.config_map()
        eosio_repository_dir = None

        _eosio_repository_dir = sys.argv[1]

        if not _eosio_repository_dir:
            _eosio_repository_dir = eosio_repository_dir

        ok = _eosio_repository_dir and os.path.exists(os.path.join(
                _eosio_repository_dir, config.node_exe_[1][0]))

        if ok:
            map = config.config_map()
            map[config.eosio_repository_dir_[0]] = _eosio_repository_dir
            config.write_config_map(map)
            break

    while True:
        map = config.config_map()
        contract_workspace_dir = None

        _contract_workspace_dir = sys.argv[2]
        if not _contract_workspace_dir:
            _contract_workspace_dir = contract_workspace_dir
        
        if _contract_workspace_dir and os.path.exists(
                _contract_workspace_dir) and os.path.isdir(
                    _contract_workspace_dir):
            map = config.config_map()
            map[config.contract_workspace_[0]] = _contract_workspace_dir
            config.write_config_map(map)
            break

        
parser = argparse.ArgumentParser(description='''
''')

parser.add_argument("root", default=None, help="WSL root path")
args = parser.parse_args()
install(args.root)
