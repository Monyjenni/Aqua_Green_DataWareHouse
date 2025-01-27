import requests
from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=['192.168.1.68:9092'],
    value_serializer=json_serializer
)

# Function to fetch data from ThingsBoard API
def fetch_thingsboard_data(url, access_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}" 
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully fetched data from ThingsBoard!")
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":

    THINGSBOARD_HOST = "localhost"  
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN" 
    DEVICE_ID = "YOUR_DEVICE_ID" 
    API_URL = f"http://{THINGSBOARD_HOST}:8080/api/v1/{DEVICE_ID}/attributes"

    while True:
        thingsboard_data = fetch_thingsboard_data(API_URL, ACCESS_TOKEN)
        
        if thingsboard_data:
            producer.send("thingsboard_data", thingsboard_data)
            print(f"Sent data to Kafka: {thingsboard_data}")
        time.sleep(5)





