import logging
import os

import boto3

logging.basicConfig(level=logging.INFO)


class S3FileDownloader:
    """S3 file downloader"""

    def __init__(self, bucket_name: str, local_folder: str):
        """
        Args:
            bucket_name (str): Name of the S3 bucket
            local_folder (str): Local folder where the files will be downloaded
        """
        self.bucket_name = bucket_name
        self.local_folder = local_folder
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )

    def download_file(self, s3_key: str):
        """
        Download a file from S3. Otherwise, copy it from the local path

        Args:
            s3_key (str): Key of the file in S3
        """
        if not os.path.exists(self.local_folder):
            os.mkdir(self.local_folder)

        # TODO: Modifikovati tako da skida fajl samo ukoliko fajl u s3 promenjen u odnosu na lokalni
        try:
            self.s3.download_file(
                self.bucket_name, s3_key, f"{self.local_folder}/{s3_key.split('/')[-1]}"
            )
            logging.info(f"File {s3_key} downloaded from S3")
        except Exception as e:
            logging.exception(e)
