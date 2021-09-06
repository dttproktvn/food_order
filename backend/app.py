from flask import Flask, request, jsonify
import sys
import json
# TODO: manage sys path at config file
sys.path.append('/home/tony/Desktop/food-order/backend/controllers')
import sign_up_controller
app = Flask(__name__)


@app.route('/status-check')
def hello():
    return {"status":"ok"}

@app.route('/signup', methods = ['POST'])
def signup():
    json_data = request.json
    userID = json_data["id"]
    password = json_data["password"]
    return sign_up_controller.signup(userID,password)



app.run(host="0.0.0.0")