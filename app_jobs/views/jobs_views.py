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

app_jobs = Blueprint("app_jobs",__name__)

@app_jobs.route("/jobs",methods=["POST"])
def post():
    jobs_data = request.get_json()
    jobs = create(jobs_data)
    return jsonify(jobs.serialize()),201

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
