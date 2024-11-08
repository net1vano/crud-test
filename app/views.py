from flask import render_template
from app import app
from app.forms import ButtonForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    button = ButtonForm()
    return render_template("buttons.html", form=button)
