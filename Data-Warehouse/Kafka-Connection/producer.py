from kafka import KafkaProducer
import json
from data import get_registered_user  # Corrected the import statement
import time

# Function to serialize data to JSON
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# Create the Kafka producer with the JSON serializer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer
)

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        print(f"Sent: {registered_user}")
        time.sleep(4)
