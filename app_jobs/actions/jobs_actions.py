from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy import Date

from app_jobs.models.jobs_models import Jobs
from database.database import save
from database.database import commit
from database.database import db


def create(data:dict) -> Jobs:
    return save(
        Jobs(
            user_id = data['user_id'],
            function = data['function'],
            enterprise = data['enterprise'],
            date_begin = data['date_begin'],
            date_out = data['date_out'],
            activities = data['activities']
        )
    )

def get_job_by_id(job_id:int) -> Jobs:
    job = Jobs.query.filter_by(id_job=job_id).first()
    return job

def get_all_jobs() -> dict:
    all_job = Jobs.query.all()
    return all_job

def get_all_jobs_from_one_user(id:int) -> dict:
    all_job_from_user = Jobs.query.filter_by(user_id=id).first()
    return all_job_from_user

def update_job(job_id:int,new_data:dict) -> Jobs:
    job = Jobs.query.get(job_id)
    job.function = new_data['function'],
    job.enterprise = new_data['enterprise'],
    job.date_begin = new_data['date_begin'],
    job.date_out = new_data['date_out'],
    job.activities = new_data['activities']
    commit()
    return job

def delete_job(job_id:int) -> str:
    Jobs.query.filter_by(id_job=job_id).delete()
    commit()
    return "Experiência Profissional excluída com sucesso."