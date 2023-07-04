import unittest
from unittest import mock
from app import execute_script
from fastapi import status
import json
from models.script_data import ScriptData


class TestWholePipeline(unittest.TestCase):
    @mock.patch("app.CONFIG", {"script_path": "tests/integration/test_data"})
    @mock.patch("s3_manipulator.S3FileDownloader.download_file")
    def test_execute_script_module(self, mock_download_file):
        mock_download_file.return_value = None

        data = ScriptData(input_data=1, script_name="script.py")

        response = execute_script(data)
        content = json.loads(response.body.decode("utf-8"))

        self.assertEqual(content["output"], "11")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == "__main__":
    unittest.main()
