from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from datetime import datetime
from dotenv import load_dotenv
import uuid
import os, json

app = Flask(__name__)
CORS(app)

data = {}
load_dotenv(os.getenv('ENV_FILE', '.env'))
#

with open("./config/config.json") as json_config_file:
    data = json.load(json_config_file)

# app.config["MONGO_URI"] = 'mongodb://' + data['CONFIG_MONGODB_USERNAME'] + ':' + data['CONFIG_MONGODB_ADMINPASSWORD'] + '@' + data['DB_HOST'] + ':27017/' + 'notesDB'
app.config["MONGO_URI"] = 'mongodb://' + data['DB_HOST'] + ':27017/' + 'notesDB'
mongo = PyMongo(app)
expire_seconds =data['EXPIRE']



@app.route('/', methods=["GET"])
def endpoint1():
    return app.config["MONGO_URI"], 200


@app.route('/save', methods=["POST"])
def endpoint2():
    today = datetime.today()

    try:

        id = str(uuid.uuid4())[:8]
        mongo.db.notes.insert_one({"note": str(request.data.decode()), "id": id, "date": str(today)})
        return id, 200

    except:
        return "error when adding to DB", 500


@app.route('/<noteid>', methods=["GET", "DELETE"])
def endpoint3(noteid):
    if request.method == "GET":
        try:
            obj = mongo.db.notes.find_one({"id": str(noteid)})

            note = obj["note"]

            date_time = obj["date"]
            split = str(date_time).split(" ")

            date1 = datetime.fromisoformat(date_time)

            today = datetime.today()
            difference_sec = (today - date1).seconds

            if (difference_sec <= int(expire_seconds)):
                #
                try:
                    mongo.db.notes.delete_one({"id": str(noteid)})
                    return note, 200
                except:
                    return "Error while deletion", 500
            else:
                return "The Note is expired", 200


        except:
            return "Note not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=data['PORT'], debug=True)
