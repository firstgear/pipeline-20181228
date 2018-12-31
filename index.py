import json
def handler(event, context):
    message = "Hello, is it me your're looking for? Dec 31."
    return {
        "statusCode": 200,
        "body" : json.dumps(message)
    }
