import unittest
from types import ModuleType

from utils import import_script_module, read_yaml_file


class TestImportScriptModule(unittest.TestCase):
    def test_import_script_module(self):
        script_path = "tests/unit/test_data/script.py"

        module = import_script_module(script_path)
        self.assertIsInstance(module, ModuleType)

        output = module.run(1)
        self.assertEqual(output, 2)

    def test_read_yaml_file(self):
        file_path = "tests/unit/test_data/test.yaml"

        result = read_yaml_file(file_path)

        self.assertEqual(result, {"key": "value"})


if __name__ == "__main__":
    unittest.main()
