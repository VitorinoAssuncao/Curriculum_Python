from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from app_user.settings import DEBUG
from app_user.settings import HOST
from app_user.settings import PORT

from app_user.actions.user_actions import create
from app_user.actions.user_actions import login
from app_user.actions.user_actions import get_user_by_id
from app_user.actions.user_actions import get_all_user
from app_user.actions.user_actions import update_user
from app_user.actions.user_actions import delete_user
from app_user.validations.user_validations import validate_creation_data
app_user = Blueprint("app_user",__name__)

@app_user.route("/users",methods=["POST"])
def post():
    user_data = request.get_json()
    result = validate_creation_data(user_data) 
    if result == True:
        user = create(user_data)
        return jsonify(user.serialize()),201
    else:
        return result

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

@app_user.route("/users/<user_id>",methods=["PUT"])
def update(user_id:int):
    update_data = request.get_json()
    updated_user = update_user(user_id,update_data)
    return jsonify(updated_user.serialize())

@app_user.route("/users/<user_id>",methods=["DELETE"])
def delete(user_id:int):
    result =  delete_user(user_id)
    return result,200