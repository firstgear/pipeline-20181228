import json
def handler(event, context):
    message = "Welcome to release candidate2."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
