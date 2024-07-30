import json
import boto3

def lambda_handler(event, context):

    client = boto3.client('dynamodb')
    result = 0
    try:
        item = client.get_item(
            TableName='george-cloud-resume-table',
            Key={
                "variables": {
                    'S': 'counter'
                }
            })
        result = item["Item"]["value"]["N"]
        
    except Exception as ex:
        template = "An exception of type {0} occurred."
        message = template.format(ex.__class__.__name__)
        result = message
        
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET" 
        },
        "body": json.dumps({
            "value": result
        }),
    }
    
    