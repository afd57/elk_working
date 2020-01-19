import random
import time
from pymongo import MongoClient
from datetime import datetime



def generate_random_data(client):
    mydb = client["elk"]
    mycol = mydb["tempeture"]
    cur_time = datetime.now()
    random.seed(cur_time)
    tempeture = random.randrange(10,40)
    mycol.insert_one({"time": cur_time, "tempeture":int(tempeture)})
    print({"time": cur_time, "tempeture":int(tempeture)})

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    mydb = client["elk_example"]
    mycol = mydb["tempeture"]
    mycol.create_index("time")
    mycol.create_index("tempeture")
    while True:
        generate_random_data(client)
        time.sleep(5)