import sys
import json
# TODO: manage sys path at config file
sys.path.append('/home/tony/Desktop/food-order/backend/models')
from userMD import User
defaultRole = "user"
defaultStatus = "inactive"
def signup(id, password):
    newUser = User(id,password,defaultRole,defaultStatus)
    value = newUser.insert_into_db()
    if (type(value) == int):
        if (value == 0):
            print("Exception when signup")
        return {"code":value}   
    if value == True:
        print("add new user successfully")
        return {"code":200}
    if value == False:
        print("fail while add new user")
        return {"code":2}

