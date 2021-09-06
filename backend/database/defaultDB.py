import asyncio
from pymongo import MongoClient
connStr = "mongodb://admin:admin@192.168.24.135:27017/"

# Check if a db exists or not
# return value:
# True: db exists
# False: db not exists
# 0: exception
def check_existed_db(dbName):
    try:
        client = MongoClient(connStr)
        listOfDb = client.list_database_names()
        if dbName in listOfDb:           
            return True
        else:
            print("db not exists")
            return False
    except Exception as e:
        print("fail to check db exists")
        print(e)
        return 0     
#-----------------------------------------------------------------------------------#



# Create new mongodb db with a collection and record
# return value:
# 0: exception 
# 1: database exists
# True: create successfully
# False: create fail
def create_new_db(dbName, dbCollection, dbDocument):
    try:
        isDBExisted = check_existed_db(dbName)         
        if (type(isDBExisted) == int) and (isDBExisted == 0):          
            return 0
        elif isDBExisted == True:
            print("Could not create new")
            return 1
        else:
            client = MongoClient(connStr)       
            print("creating new database")
            db = client[dbName]
            collection = db[dbCollection]
            record = dbDocument
            x = collection.insert_one(dbDocument)
            return True
    except Exception as e:
        print("could create and init database")
        print(e)
        return 0
#-----------------------------------------------------------------------------------#



#check if a collection is exists:
# return value:
# True: collection exists
# False: db not exists
# 0: exception
def check_exsisted_collection(dbName,dbCollection):
    try:
        isDBExisted = check_existed_db(dbName)     
        if (type(isDBExisted) == int) and (isDBExisted == 0):           
            return 0        
        if isDBExisted == True:           
            client = MongoClient(connStr)  
            db = client[dbName]
            list_collection_names = db.list_collection_names()
            if dbCollection in list_collection_names:
                return True
            else: 
                print("collection doesn't exist")
                return False            
        else:           
            return False
    except Exception as e:      
        print("exception")
        print(e)
        return 0   
#-----------------------------------------------------------------------------------#



#Check if a field value is existed in a collection. ex: {"_id":"admin}" 
# return value:
# True:  field value exists
# False: field value doesn't exist
# 0: exception
def check_exsisted_field(dbName,dbCollection, dbDocument_fields):
    try:
        isCollectionExisted = check_exsisted_collection(dbName,dbCollection)
        if (type(isCollectionExisted) == int) and (isCollectionExisted == 0):
            return 0
        if isCollectionExisted == False:
            return False
        client = MongoClient(connStr)  
        db = client[dbName]
        collection = db[dbCollection]
        dbDocument = collection.find_one(dbDocument_fields)
        if dbDocument == None:
            return False
        return True
    except Exception as e:
        print("fail to check db exists")
        print(e)
        return 0 
#-----------------------------------------------------------------------------------#


#Insert a document into a collection.
# return value:
# True:  insert successfully
# False: insert fail
# 0: exception
def insert_document(dbName,dbCollection,dbDocument):
    try:
        isCollectionExisted = check_exsisted_collection(dbName,dbCollection)
        if (type(isCollectionExisted) == int) and (isCollectionExisted == 0):
            return 0
        if isCollectionExisted == False:
            return False
        client = MongoClient(connStr)  
        db = client[dbName]
        collection = db[dbCollection]
        collection.insert_one(dbDocument)
        return True
    except Exception as e:
        print("fail to insert documents")
        print(e)
        return 0
#-----------------------------------------------------------------------------------#



#testing
#TODO: remove when release
# dbDocument = {"_id":"admin1",
#                 "password":"123456Abc'",
#                 "role":"admin",
#                 "status":"active"
#             }
        
# a = insert_document("food_order","users",dbDocument)
# print(a)