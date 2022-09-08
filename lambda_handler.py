from unittest import result
import boto3

def get_model():
    """
    Download model object from AWS S3
    """
    bucket = boto3.resource("S3").Bucket("<enter_bucket_name>")
    bucket.download_fileobj(Key="model/model.pkl")


def predict(event):
    """
    Takes an event as input and returns model output

    """
    # Extract body
    body = event["body"]
    model = get_model()
    model.predict(body)
    return result

def lambda_handler(event, context):
    """
    Execute model predictions with a given event prompt
    
    """
    result = predict(event)
    return {"statusCode": 200,
            "body": result}