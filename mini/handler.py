import json
import time

def mini(event, context):
    ct = round( time.time() )
    body = {
        "message": "Automation for the People",
        "timestamp": str(ct)
    }

    response = {
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
