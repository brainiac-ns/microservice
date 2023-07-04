import importlib.util
from types import ModuleType
from typing import Dict

import yaml


def import_script_module(script_path: str) -> ModuleType:
    """
    Import the script as a module

    Args:
        script_path (str): Path to the script file

    Returns:
        module: Script module
    """
    spec = importlib.util.spec_from_file_location("script_module", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# TODO: Unit test
def read_yaml_file(file_path: str) -> Dict:
    """
    Read and parse a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed YAML content as a dictionary.
    """
    with open(file_path, "r") as file:
        yaml_content = yaml.safe_load(file)
    return yaml_content
