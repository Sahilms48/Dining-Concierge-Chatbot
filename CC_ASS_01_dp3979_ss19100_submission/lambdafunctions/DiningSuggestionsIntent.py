import json
import boto3
import uuid
import logging

# Initialize the Lex client
sqs = boto3.client('sqs')

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_lex_request(event):
    """Handles a request from Lex."""
    slots = event['currentIntent']['slots']
    location = slots.get('location')
    cuisine = slots.get('cuisine')
    dining_time = slots.get('dining_time')
    number_people = slots.get('number_people')
    email = slots.get('email')

    # Check if all slots are filled
    if all([location, cuisine, dining_time, number_people, email]):
        # Push the collected information to an SQS queue
        params = {
            'MessageBody': json.dumps({
                'location': location,
                'cuisine': cuisine,
                'dining_time': dining_time,
                'number_people': number_people,
                'email': email,
            }),
            'QueueUrl': 'https://sqs.us-east-1.amazonaws.com/423623832978/chatBot',
        }

        try:
            sqs.send_message(**params)
            response = {
                'dialogAction': {
                    'type': 'Close',
                    'fulfillmentState': 'Fulfilled',
                    'message': {
                        'contentType': 'PlainText',
                        'content': "You're all set. Expect my suggestions shortly. Have a good day.",
                    },
                },
            }
            return response
        except Exception as e:
            logger.error(f"Error sending message to SQS: {str(e)}")
            return {
                'dialogAction': {
                    'type': 'Close',
                    'fulfillmentState': 'Failed',
                    'message': {
                        'contentType': 'PlainText',
                        'content': 'Failed to process your request.',
                    },
                },
            }
    
    # If not all slots are filled, delegate back to Lex
    return {
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots,
        },
    }

def lambda_handler(event, context):
    """Main Lambda handler for Lex."""
    logger.info(f"Received event: {json.dumps(event)}")

    if 'currentIntent' in event:
        # Request from Lex
        return handle_lex_request(event)
    
    return {
        'statusCode': 400,
        'body': json.dumps({'code': 400, 'message': 'Invalid request format'}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
