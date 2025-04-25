import configparser
from confluent_kafka import Consumer
from pymongo import MongoClient
import json

# === PHẦN A: ĐỌC DỮ LIỆU TỪ KAFKA NGUỒN ===

# Đọc cấu hình từ file config.ini
config = configparser.ConfigParser()
config.read('config.ini')

kafka_conf = dict(config['kafka_source'])

# Chuyển đổi key cho đúng định dạng confluent_kafka
kafka_settings = {
    'bootstrap.servers': kafka_conf['bootstrap_servers'],
    'security.protocol': kafka_conf['security_protocol'],
    'sasl.mechanisms': kafka_conf['sasl_mechanisms'],
    'sasl.username': kafka_conf['sasl_username'],
    'sasl.password': kafka_conf['sasl_password'],
    'group.id': kafka_conf['group_id'],
    'auto.offset.reset': kafka_conf['auto_offset_reset'],
}
topic = kafka_conf['topic']

# === PHẦN B: GHI VÀO MONGODB ===

mongo_conf = dict(config['mongodb'])
mongo_client = MongoClient(mongo_conf['uri'])
db = mongo_client[mongo_conf['database']]
collection = db[mongo_conf['collection']]

def save_to_mongo(data):
    """
    Ghi một document vào MongoDB.
    Nếu data không phải JSON hợp lệ, sẽ lưu dưới dạng raw string.
    """
    try:
        doc = json.loads(data)
    except Exception:
        doc = {'raw': data}
    result = collection.insert_one(doc)
    print(f"Inserted document with _id: {result.inserted_id}")

def consume_kafka_and_save():
    """
    Đọc message từ Kafka và lưu vào MongoDB.
    """
    consumer = Consumer(kafka_settings)
    consumer.subscribe([topic])
    print(f"Listening on topic '{topic}'...")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            data = msg.value().decode('utf-8')
            print(f"Received message: {data}")
            save_to_mongo(data)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_kafka_and_save()
