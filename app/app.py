from flask import render_template, redirect, request
from app import app
from app.forms import *
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    buttons = Buttons()
    return render_template("buttons.html", buttons=buttons)

#TODO добавить логику в функции + подключить дб, поменять кнопки в html на js чтобы реализовать put и delete
#TODO html Имеет только POST и GET
@app.route('/api ', methods=['GET', 'POST'])
def create_request():
    print(request.method)
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_request():
    print(request.method)
    if request.method == "GET":
        pass
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        pass