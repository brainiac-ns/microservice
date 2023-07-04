# microservice
Python microservice using REST architecture

## Running with Docker
```shell
docker build -t microservice .
docker run -p 8000:8000 -e AWS_ACCESS_KEY_ID=_aws_key_ -e AWS_SECRET_ACCESS_KEY=_aws_secret_ microservice
```

## Running without Docker
```shell
cd src
AWS_ACCESS_KEY_ID=_aws_key_ AWS_SECRET_ACCESS_KEY=_aws_secret_ python app.py
```

### How it works

Microservice will first try to download a script from the S3 bucket. If that is not possible,
it will try to copy it from local storage. After that the file will be imported and the function
__run__ will be executed. 