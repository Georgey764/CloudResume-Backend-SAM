import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    new_value = 0
    
    try:
        response = response = client.update_item(
            TableName="george-cloud-resume-table",
            ExpressionAttributeNames={
                '#V': 'value',
            },
            ExpressionAttributeValues={
                ':v': {
                    'N': '1'
                }
            },
            Key={
                'variables': {
                    'S': 'counter'
                }
            },
            UpdateExpression="ADD #V :v",
            ReturnValues="ALL_NEW"
        )
        new_value = response["Attributes"]
    except Exception as exception:
        if type(exception).__name__ == 'ValidationException':
            response = client.put_item(
                TableName="george-cloud-resume-table",
                Item={
                    "variables": {
                        "S": "counter"
                    },
                    "value": {
                        "N": "1"
                    }
                }
            )
            new_value = response["Attributes"]
        else:
            raise
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET" 
        },
        "body": json.dumps({
            "updated_item": new_value
        }),
    }
