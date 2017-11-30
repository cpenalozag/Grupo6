from kafka import KafkaConsumer
import time
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import datetime





# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('alta.fueraDeRango',
                         group_id='my-group',
                         bootstrap_servers=['172.24.42.23:8090','172.24.42.63:8090','172.24.42.24:8090'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("hola")
    jsonVal=json.loads(message.value)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))