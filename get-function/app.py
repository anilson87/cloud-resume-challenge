import json

# import requests


def get-function(event, context):

    return {
         "statusCode": 200,
	   
        "body": json.dumps(
            {
                "message": "get world",
            }
        ),
       
    }
