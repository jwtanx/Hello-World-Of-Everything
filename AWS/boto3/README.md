# Boto3

## Installation
```sh
pip install boto3
```

## Credentials
```sh
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
```

## Services
```py
import boto3
services = boto3.session.Session().get_available_services()
```

## Paginator
https://stackoverflow.com/questions/47585842/aws-s3-in-boto3-how-to-move-to-next-page-by-paginator-of-s3-in-boto3
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html
Difference between max_items and page_size
- `max_items`: The maximum number of items to retrieve in total
- `page_size`: The maximum number of items to retrieve per page