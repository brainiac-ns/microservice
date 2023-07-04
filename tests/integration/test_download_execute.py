import unittest

from app import execute_script


class TestWholePipeline(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_import_script_module(self):
        execute_script("")

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
