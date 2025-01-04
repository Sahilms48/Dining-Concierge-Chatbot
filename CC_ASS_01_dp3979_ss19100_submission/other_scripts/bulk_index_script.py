import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, helpers
from requests_aws4auth import AWS4Auth
import sqlite3

# AWS Configuration
region = 'us-east-1'  # replace with your region
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# OpenSearch Configuration
host = 'search-restaurants-search-etm4h4vb7fuy45sxt4cui3xuai.us-east-1.es.amazonaws.com'  # replace with your endpoint
index_name = 'restaurants'

# Create the OpenSearch client
client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# Create index if it doesn't exist
if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name, body={
        "mappings": {
            "properties": {
                "RestaurantID": {"type": "keyword"},
                "Cuisine": {"type": "keyword"}
            }
        }
    })

# Connect to SQLite database
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()

# Fetch data from SQLite
cursor.execute("SELECT business_id, cuisine FROM restaurants")
restaurants = cursor.fetchall()

# Prepare bulk data
def generate_bulk_data():
    for restaurant in restaurants:
        yield {
            "_index": index_name,
            "_source": {
                "RestaurantID": restaurant[0],
                "Cuisine": restaurant[8]  # Changed from [8] to [1] as per the SELECT statement
            }
        }

# Perform bulk indexing
success, _ = helpers.bulk(client, generate_bulk_data())

print(f"Indexed {success} documents")

# Close connections
conn.close()
client.close()