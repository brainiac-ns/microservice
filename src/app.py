import logging
import os

import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.script_data import ScriptData
from s3_manipulator import S3FileDownloader
from utils import import_script_module

logging.basicConfig(level=logging.INFO)

app = FastAPI()


S3_FILE_DOWNLOADER = S3FileDownloader(
    bucket_name=os.getenv("BUCKET_NAME", default="mlops-task"),
    local_path=os.getenv("LOCAL_FILES", default="../automated-cicd"),
)


# TODO: Test integracioni
# TODO: Koji bi queue ovde koristio?
# TODO: Nacrtati dijagram kako sve ovo komunicira (cicd + microservice)
@app.post("/execute_script")
def execute_script(data: ScriptData) -> dict:
    """
    Execute a script from a Storage and return the output

    Args:
        data (ScriptData): Input data for the script

    Returns:
        dict: Output of the script
    """
    try:
        S3_FILE_DOWNLOADER.download_file(f"scripts/{data.script_name}")

        script_module = import_script_module(f"scripts/{data.script_name}")

        output = script_module.run(data.input_data)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"output": output},
        )
    except Exception as e:
        logging.exception(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": e},
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
