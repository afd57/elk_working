from datetime import datetime
from elasticsearch import Elasticsearch
import random
import time

# by default we connect to localhost:9200
es = Elasticsearch()
# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.create(index='my-weather', ignore=400)
random.seed(30)
for _ in range(30):
    # datetimes will be serialized
    res = es.index(index="my-weather", body={"temperature": random.randint(10, 40), "time": datetime.now()})
    print(res)
    time.sleep(5)
    # es.get(index="my-index", id=42)['_source']
