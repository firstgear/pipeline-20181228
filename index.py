import json
def handler(event, context):
    message = "Welcome to the serverless session in 2019 in Amsterdam."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
