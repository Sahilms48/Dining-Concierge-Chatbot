import boto3
import sqlite3
from decimal import Decimal

# Set up AWS credentials and DynamoDB client
session = boto3.Session(profile_name='default')
dynamodb = session.resource('dynamodb')

# Create the DynamoDB table
table_name = 'yelp-restaurants'
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'business_id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'business_id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    print(f"Table {table_name} created successfully")
except dynamodb.meta.client.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists")
    table = dynamodb.Table(table_name)

# Connect to SQLite database
sqlite_conn = sqlite3.connect('restaurants.db')
cursor = sqlite_conn.cursor()

# Fetch all data from SQLite
cursor.execute("SELECT * FROM restaurants")
rows = cursor.fetchall()

# Helper function to convert float to Decimal
def float_to_decimal(f):
    return Decimal(str(f))

# Transfer data to DynamoDB
for row in rows:
    item = {
        'business_id': row[0],  # Assuming business_id is the first column
        'name': row[1],
        'address': row[2],
        'coordinates': {
            'latitude': float_to_decimal(row[3]),
            'longitude': float_to_decimal(row[4])
        },
        'review_count': row[5],
        'rating': float_to_decimal(row[6]),
        'zip_code': row[7],
        'cuisine': row[8],
        'insertedAtTimestamp': row[9]  # Assuming you have this field in your SQLite DB
    }
    
    try:
        table.put_item(Item=item)
        print(f"Added item: {item['business_id']}")
    except Exception as e:
        print(f"Error adding item {item['business_id']}: {str(e)}")

# Close SQLite connection
sqlite_conn.close()

print("Data transfer completed")