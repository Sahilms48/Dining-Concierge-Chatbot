import boto3

def lambda_handler(event, context):
    response = {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': 'You\'re welcome.',
            },
        },
    }
    return response