from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from app_user.settings import DEBUG
from app_user.settings import HOST
from app_user.settings import PORT

from app_schooling.actions.schooling_actions import create
from app_schooling.actions.schooling_actions import update_schooling
from app_schooling.actions.schooling_actions import delete_schooling
from app_schooling.actions.schooling_actions import get_all_schooling
from app_schooling.actions.schooling_actions import get_schooling_by_id
from app_schooling.actions.schooling_actions import get_all_schoolings_from_one_user

app_schooling = Blueprint("app_schooling",__name__)

@app_schooling.route("/schooling",methods=["POST"])
def post():
    schooling_data = request.get_json()
    Schooling = create(schooling_data)
    return jsonify(Schooling.serialize()),200

@app_schooling.route("/schooling/<id>",methods=["GET"])
def get_schooling(id:int):
    schooling = get_schooling_by_id(id)
    return jsonify(schooling.serialize())

@app_schooling.route("/schooling/user/<id>",methods=["GET"])
def get_all_schooling_from_one_user(id:int):
    return jsonify([schooling.serialize() for schooling in get_all_schoolings_from_one_user(id)])    

@app_schooling.route("/schooling",methods=["GET"])
def get_all():
    return jsonify([schooling.serialize() for schooling in get_all_schooling()])

@app_schooling.route("/schooling/<id>",methods=["PUT"])
def update_schooling_by_id(id:int):
    updated_data = request.get_json()
    new_schooling = update_schooling(id,updated_data)
    return new_schooling.serialize()

@app_schooling.route("/schooling/<id>",methods=["DELETE"])
def remove_schooling_by_id(id:int):
    return delete_schooling(id)