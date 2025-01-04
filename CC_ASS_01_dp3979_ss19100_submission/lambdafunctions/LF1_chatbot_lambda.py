import json
import boto3

def lambda_handler(event, context):
    # Initialize the Lex client
    client = boto3.client('lex-runtime')
    
    # Define CORS headers
    cors_headers = {
        'Access-Control-Allow-Origin': '*',  # Replace '*' with your specific origin in production
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST'
    }
    
    # Extract messages from the event body
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'message': 'Invalid JSON format in request body'})
        }
    
    messages = body.get('messages', [])
    
    if not messages:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'message': 'No messages provided'})
        }
    
    # Extract message details
    message = messages[0]
    user_id = message.get('unstructured', {}).get('id', 'defaultUser')
    text = message.get('unstructured', {}).get('text', '')
    
    if not text:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'message': 'Empty message text'})
        }
    
    # Send the message to Lex and get a response
    try:
        lex_response = client.post_text(
            botName='BookHotel',
            botAlias='chatBot',
            userId=user_id,
            inputText=text
        )
        
        # Extract Lex response details
        lex_message = lex_response.get('message', 'I’m still under development. Please come back later.')
        
        # Format Lex response into BotResponse format
        bot_response = {
            'messages': [{
                'type': 'unstructured',  # Must match frontend expectation
                'unstructured': {
                    'text': lex_message
                }
            }]
        }
        
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps(bot_response)
        }
    
    except Exception as e:
        # Log the exception details for debugging (optional)
        print(f"Error processing message: {e}")
        
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'code': 500, 'message': 'Internal server error'})
        }
