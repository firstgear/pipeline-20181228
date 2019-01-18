import json
def handler(event, context):
    message = "Welcome Ionut."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
