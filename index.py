def handler(event, context):
    message = "Hello, is it me your're looking for?"
    return {
        "statusCode": 200,
        "body" : message
    }

