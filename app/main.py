from flask import Flask
from bson.objectid import ObjectId
from flask import render_template, request, jsonify
import app.utils as utils

app = Flask(__name__)
from app.mongo import *


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("buttons.html")


@app.route('/api/', methods=["GET", "POST"])
def create_request():
    if request.method == "GET":
        result = utils.custom_serializer(list(data.find()))
        return jsonify({"request": result}), 200
    if request.method == "POST":
        cinema = utils.Cinema(name=request.json["name"],
                              session_start=request.json["start"],
                              session_end=request.json["end"])
        if not request.json.get("name") and not request.json.get("end") and not request.json.get("start"):
            cinema = utils.generate_data()  # на случай если не указаны данные - создаем рандомный фильм
        data.insert_one(cinema.to_dict())
        return jsonify({'status': 'created', "data": cinema.to_dict()}), 200
    return jsonify({"message": "unintended method"}), 403


@app.route('/api/<uid>', methods=["GET", "PUT", "DELETE"])
def update_request(uid):
    if request.method == "GET":
        item = data.find_one({"_id": ObjectId(uid)})
        item = utils.custom_serializer(item)
        return jsonify({'data': item}), 200
    if request.method == "PUT":
        filter = {"_id": ObjectId(uid)}
        update_data = {"$set": {"name": request.json["name"],
                                "start": request.json["start"],
                                "end": request.json["end"]}
                       }
        data.update_one(filter, update_data)
        return jsonify({'message': 'Элемент обновлен'}), 200
    if request.method == "DELETE":
        try:
            item = data.find_one({"_id": ObjectId(uid)})
            data.delete_one(item)
        except Exception as e:
            print(e)
        return jsonify({'message': "Элемент удален"}), 200
    return jsonify({"message": "unintended method"}), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
