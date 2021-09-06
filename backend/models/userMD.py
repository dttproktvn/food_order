import sys
import json
# TODO: manage sys path at config file
sys.path.append('/home/tony/Desktop/food-order/backend/database')
import userDB
class User:
    def __init__(self, id, password, role, status):
        self.id = id
        self.password = password
        self.role = role
        self.status = status
    

    # Insert into db
    def insert_into_db(self):
        isUserExisted = userDB.check_user_exists(self.id)
        if (type(isUserExisted) == int) and (isUserExisted == 0):
            print("Exception when checking user existed")
            return 0
        if (isUserExisted == True):
            print("user existed, cannot add new")
            return 1
        userSchema = {
            "_id" : self.id,
            "password" : self.password,
            "role" : self.role,
            "status": self.status
        }
        insertSuccess = userDB.insert_new_user(userSchema)
        if (type(insertSuccess) == int) and (insertSuccess == 0):
            print("Exception when inserting a new user")
            return 0
        return insertSuccess



