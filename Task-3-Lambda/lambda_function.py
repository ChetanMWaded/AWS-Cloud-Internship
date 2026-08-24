def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": '{"message": "Hello from InternSpark!", "status": "success"}'
    }