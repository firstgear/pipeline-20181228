import json
def handler(event, context):
    message = "Hello, is it me your're looking for? 9 Jan."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
