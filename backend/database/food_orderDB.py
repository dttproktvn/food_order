import asyncio
from pymongo import MongoClient
import defaultDB
connStr = "mongodb://admin:admin@192.168.24.135:27017/"
  

def check_db_connection(): 
    try:
        client = MongoClient(connStr)
        print(client.server_info())
        return True
    except Exception as e:
        print(e)
        return False

def init_data(): #database: food_order
    dbName = "food_order"
    dbCollection = "users"

    # TODO: model class ?
    dbDocument = {"_id":"admin",
                "password":"123456Abc'",
                "role":"admin",
                "status":"active"
    }
    initSuccess = defaultDB.create_new_db(dbName,dbCollection,dbDocument)    
    if (type(initSuccess) == int) and (initSuccess == 0):
        print("exception")
        return False
    if (type(initSuccess) == int) and (initSuccess == 1):
        print("database already exists, dont need to init")
        return True
    return initSuccess 



a = init_data()
print(a)

