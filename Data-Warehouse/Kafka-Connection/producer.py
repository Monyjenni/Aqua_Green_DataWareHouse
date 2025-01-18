from kafka import KafkaProducer

# Create the producer with the correct argument for the bootstrap server
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Send a test message
producer.send('test-topic', b'Hello Kafka!')
producer.flush()  # Ensure the message is sent
print("Message sent successfully!")
