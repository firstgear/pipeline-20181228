import json
def handler(event, context):
    message = "Welcome to Knowledge Bite session on public cloud5."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
