import defaultDB
dbName = "food_order"
dbCollection = "users"

#Check if a user id existed
#return value
# True: user exsisted
# False: user doesn't exsisted
# 0: Exception
def check_user_exists(userID):
    idValue = {"_id":userID}
    isUserExisted = defaultDB.check_exsisted_field(dbName,dbCollection,idValue)
    if (type(isUserExisted) == int) and (isUserExisted == 0):
        return 0
    return isUserExisted
#-----------------------------------------------------------------------------------#


#insert a new user into db
#return value
# True: insert successfully
# False: insert fail 
# 0: Exception
def insert_new_user(userSchema):
    insertSuccess = defaultDB.insert_document(dbName,dbCollection,userSchema)
    if (type(insertSuccess) == int) and (insertSuccess == 0):    
        return 0
    return insertSuccess

