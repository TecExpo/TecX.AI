from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(topic, message):
    producer.send(topic, message)
    producer.flush()
    print(f"Sent: {message}")

if __name__ == "__main__":
    send_message("test-topic", {"event": "New user registered"})
