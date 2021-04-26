import json
from kafka import KafkaProducer
import kafka

bootstrap_servers = 'localhost:29092'
topicName = 'wallets'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

dict_ = {}

dict_['wallet'] = 'teste_private'
dict_['private'] = 'private123456'
dict_['public']  ='public123456'

try:

    producer.send(topicName,dict_)

    metrics = producer.metrics()
    print(metrics)
    producer.flush()
except kafka.errors.KafkaError as e:
    print(e)
    