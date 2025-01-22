import json
import time
import requests
from kafka import KafkaProducer

# Function to serialize data to JSON format
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['192.168.1.68:9092'],
    value_serializer=json_serializer
)

# Function to fetch random API data
def fetch_random_api_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return {}

if __name__ == "__main__":
    while True:
        # Fetch data from API
        api_data = fetch_random_api_data()
        
        if api_data:
            print(f"Fetched API data: {api_data}")

            # Send data to Kafka topic
            producer.send("random_api_data", api_data)
            print("Data sent to Kafka topic 'random_api_data'")

        # Sleep before fetching again
        time.sleep(5)
