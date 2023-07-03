import logging
import os

import boto3

logging.basicConfig(level=logging.INFO)


# TODO: Testovi
class S3FileDownloader:
    """S3 file downloader"""

    def __init__(self, bucket_name: str, local_path: str):
        """
        Args:
            bucket_name (str): Name of the S3 bucket
            local_path (str): Local path to download the file
        """
        self.bucket_name = bucket_name
        self.local_path = local_path
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
        if not os.path.exists("scripts"):
            os.mkdir("scripts")

    def download_file(self, s3_key: str):
        """
        Download a file from S3. Otherwise, copy it from the local path

        Args:
            s3_key (str): Key of the file in S3
        """
        # TODO: Modifikovati tako da skida fajl samo ukoliko fajl u s3 promenjen u odnosu na lokalni
        try:
            self.s3.download_file(self.bucket_name, s3_key, s3_key)
            logging.info(f"File {s3_key} downloaded from S3")
        except Exception:
            self.copy_from_local_path(s3_key)

    def copy_from_local_path(self, s3_key: str):
        """
        Copy a file from the local path

        Args:
            s3_key (str): Key of the file in S3
        """
        try:
            logging.info(f"Copying file  {self.local_path}/{s3_key} from local path")
            os.system(f"cp {self.local_path}/{s3_key} {s3_key}")
        except Exception as e:
            logging.exception(e)
            logging.warn("File does not exist in local path")
