import json
from kafka import KafkaProducer
import kafka

bootstrap_servers = 'localhost:29092'
topicName = 'qwe'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

dict_ = {}

dict_['address'] = 'address'
dict_['private'] = 'private'
dict_['public']  ='public'

try:

    producer.send(topicName,dict_)

    metrics = producer.metrics()
    print(metrics)
    producer.flush()
except kafka.errors.KafkaError as e:
    print(e)
    