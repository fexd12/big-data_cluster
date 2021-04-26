#!/bin/sh

echo "Starting Sink"
curl -s \
     -X POST http://kafka-connect:8083/connectors \
     -H "Content-Type: application/json" \
     -d '{
  "name": "wallets-sink",
  "config":{
    "connector.class": "com.datastax.oss.kafka.sink.CassandraSinkConnector",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",  
    "key.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable":"false",
    "tasks.max": "1",
    "topics": "wallets",
    "contactPoints": "host.docker.internal",
    "loadBalancing.localDc": "datacenter1",
    "topic.wallets.bitcoin.address.mapping": "address=value.wallet, private_key=value.private, public_key=value.public"
  }
}'
# ,"topic.wallets.bitcoin.address.consistencyLevel": "LOCAL_QUORUM"
 
echo "Done."