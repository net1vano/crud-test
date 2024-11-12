import json

from flask import render_template, redirect, request, url_for, jsonify
from app import app
from app.forms import *
from pymongo import MongoClient

from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/"}})
print(CORS)


client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("buttons.html")

#TODO добавить логику в функции + подключить дб, поменять кнопки в html на js чтобы реализовать put и delete
#TODO html Имеет только POST и GET

@app.route('/api/', methods=["GET", "POST"])
def create_request():
    print(request.method)
    if request.method == "GET":
        return jsonify({'message': 'OK'}), 200
    if request.method == "POST":
        return jsonify({'message': 'OK'}), 200
    return jsonify({'status': "ok", 'request': request.method})

@app.route('/api/<int:uid>', methods=["GET", "PUT", "DELETE"])
def update_request(uid):
    print(request.method)
    if request.method == "GET":
        return jsonify({'message': 'Элемент создан', 'data': 'data'}), 201
    if request.method == "PUT":
        return jsonify({'message': 'Элемент обновлен', 'data': 'data'}), 200
    if request.method == "DELETE":
        return jsonify({'message': 'Элемент удален'}), 204
    return jsonify({'message': 'OK'}), 200
