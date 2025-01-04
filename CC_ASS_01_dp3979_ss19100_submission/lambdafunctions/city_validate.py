import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_location(location):
    """Validates if the given location is Manhattan."""
    if location.lower() == 'manhattan':
        return True
    return False

def elicit_slot(intent_name, slots, slot_to_elicit, message):
    """Informs Lex to ask for a specific slot (e.g., location) again."""
    return {
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': {
                'contentType': 'PlainText',
                'content': message
            }
        }
    }

def lambda_handler(event, context):
    """Main Lambda handler to validate the location slot."""
    logger.info(f"Received event: {json.dumps(event)}")

    intent_name = event['currentIntent']['name']
    slots = event['currentIntent']['slots']
    location = slots.get('location')

    # If location is provided, validate it
    if location:
        if validate_location(location):
            # If valid (Manhattan), continue with the next step of the conversation
            return {
                'dialogAction': {
                    'type': 'Delegate',
                    'slots': slots
                }
            }
        else:
            # If invalid, ask for the location again
            return elicit_slot(intent_name, slots, 'location', f"Sorry, we only support Manhattan as a location. Please provide a valid location.")
    
    # If no location is provided, delegate back to Lex
    return {
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }
