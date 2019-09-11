import json
def handler(event, context):
    message = "Welcome to SAM driven API."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
