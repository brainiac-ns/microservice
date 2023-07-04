import importlib.util
from types import ModuleType


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
