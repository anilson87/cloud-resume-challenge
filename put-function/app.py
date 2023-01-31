import json

# import requests


def put-function(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "put world",
            }
        ),
       
    }
