from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from app_user.settings import DEBUG
from app_user.settings import HOST
from app_user.settings import PORT

from  app_jobs.actions.jobs_actions import create
from  app_jobs.actions.jobs_actions import get_job_by_id
from  app_jobs.actions.jobs_actions import get_all_jobs
from  app_jobs.actions.jobs_actions import get_all_jobs_from_one_user
from  app_jobs.actions.jobs_actions import update_job
from  app_jobs.actions.jobs_actions import delete_job

from app_jobs.validations.jobs_validations import validate_jobs_data

app_jobs = Blueprint("app_jobs",__name__)

@app_jobs.route("/jobs",methods=["POST"])
def post():
    jobs_data = request.get_json()
    result = validate_jobs_data(jobs_data)

    if result == True:
        jobs = create(jobs_data)
        return jsonify(jobs.serialize()),201
    else:
        return result,400

@app_jobs.route("/jobs/<id>",methods=["GET"])
def get_job_experience_by_id(id:int):
    job = get_job_by_id(id)
    return jsonify(job.serialize())

@app_jobs.route("/jobs/user/<id>",methods=["GET"])
def get_all_jobs_from_one_user(id:int):
    return jsonify([jobs.serialize() for jobs in get_all_jobs_from_one_user(id)])    

@app_jobs.route("/jobs",methods=["GET"])
def get_all():
    return jsonify([jobs.serialize() for jobs in get_all_jobs()])

@app_jobs.route("/jobs/<id>",methods=["PUT"])
def update_job_by_id(id:int):
    updated_data = request.get_json()
    new_job = update_job(id,updated_data)
    return new_job.serialize()

@app_jobs.route("/jobs/<id>",methods=["DELETE"])
def remove_job_by_id(id:int):
    return delete_job(id)