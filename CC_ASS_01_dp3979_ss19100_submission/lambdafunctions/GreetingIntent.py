import boto3

def lambda_handler(event, context):
    response = {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': 'Hi there, I am a chatbot',
            },
        },
    }
    return response