from flask import render_template, redirect, request
from app import app
from app.forms import *
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

data = {"1": "asd", "2": "qwe", "3": "zxc"}

@app.route('/')
@app.route('/index', methods=['GET', 'POST', 'DELETE', 'PUT'])
def index():
    buttons = Buttons()
    return render_template("buttons.html", buttons=buttons)


@app.route('/request', methods=['GET'])
def read_request():
    req = request.args.get("read")
    print(req)
    #print(*args, **kwargs)
    return "get_request"

@app.route('/request', methods=['POST'])
def create_request():
    req = request.args.get("create")
    print(req)
    return "create_request"
@app.route('/request/<id>', methods=['POST'])
def update_request():
    print(f"request: {request.form.to_dict()}")
    return "update_request"

@app.route('/request/<id>', methods=['POST']) #id
def delete_request():
    req = request.args.get("update")
    return "delete_request"
