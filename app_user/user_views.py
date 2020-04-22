from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from app_user.settings import DEBUG
from app_user.settings import HOST
from app_user.settings import PORT

from  app_user.user_actions import create
from  app_user.user_actions import login
from  app_user.user_actions import get_user_by_id
from  app_user.user_actions import get_all_user

app_user = Blueprint("app_user",__name__)

@app_user.route("/users",methods=["POST"])
def post():
    user_data = request.get_json()
    user = create(user_data)
    return jsonify(user.serialize()),201

@app_user.route("/users/login",methods=["POST"])
def login_user():
    login_data = request.get_json()
    login_result = login(login_data['login'],login_data['password'])
    if login_result == False:
        return "Senha Invalida",400
    else:
        return jsonify(login_result.serialize()),200

@app_user.route("/users/<id>",methods=["GET"])
def get_user(id:int):
    user = get_user_by_id(id)
    return jsonify(user.serialize()),200

@app_user.route("/users",methods=["GET"])
def get_all():
    return jsonify([user.serialize() for user in get_all_user()])
