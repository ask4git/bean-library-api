from typing import Any

import boto3
from botocore.exceptions import ClientError


# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
def create_presigned_post(bucket_name: str, object_name: str,
                          fields: dict = None, conditions: list = None,
                          expiration: int = 3600) -> ClientError | Any:
    """Generate a presigned URL S3 POST request to upload a file
    condition specs: https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html
    :param bucket_name: Name of the S3 bucket.
    :param object_name: Name of the object in the S3 bucket.
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(
            bucket_name,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration
        )
    except ClientError as e:
        return e

    # The response contains the presigned URL and required fields
    return response
