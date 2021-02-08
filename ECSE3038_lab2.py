from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Super fancy database
PROFILE = {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "dougy",
            "role": "Engineering Student",
            "color": "#00FFFF"
        }
    }

tankDB = []
count = 0

@app.route("/")
def home():
    return "ECSE3038 - Lab 2"


@app.route("/profile", methods=["GET"])
def get_profile():
    return jsonify(PROFILE)


@app.route("/profile", methods=["POST"])
def post_profile():
    # Get date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    PROFILE[0]["data"]["last_updated"] = (dt)
    PROFILE[0]["data"]["username"] = (request.json["username"])
    PROFILE[0]["data"]["role"] = (request.json["role"])
    PROFILE[0]["data"]["color"] = (request.json["color"])

    return jsonify(PROFILE)


@app.route("/profile", methods=["PATCH"])
def patch_profile():
    # Get date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")

    PROFILE[0]["data"]["last_updated"] = (dt)
    BUF = request.json

    if "username" in BUF:
        PROFILE[0]["data"]["username"] = (BUF["username"])
    if "role" in BUF:
        PROFILE[0]["data"]["role"] = (BUF["role"])
    if "color" in BUF:
        PROFILE[0]["data"]["color"] = (BUF["color"])

    return jsonify(PROFILE)


@app.route("/data")
def get_data():
    return jsonify(tankDB)


@app.route("/data", methods=["POST"])
def post_data():
    global count
    count += 1
    a = {}
    a = request.json
    a["id"] = count
    tankDB.append(t)
    return jsonify(t)


@app.route('/data/<int:id>', methods=["PATCH"])
def patch_data(id):
    tankDB_data = request.json

    for stuff in tankDB:
        if stuff["id"] == id:
            stuff["location"] = tankDB_data["location"]
            stuff["lat"] = tankDB_data["lat"]
            stuff["long"] = tankDB_data["long"]
            stuff["percentage_full"] = tankDB_data["percentage_full"]
            break
    return jsonify(tankDB[id-1])


@app.route('/data/<int:id>', methods=["DELETE"])
def delete_data(id):
    tankDB.remove(tankDB[id-1])
    del = {
        "success": True,
    }
    return jsonify(del)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=3000
    )