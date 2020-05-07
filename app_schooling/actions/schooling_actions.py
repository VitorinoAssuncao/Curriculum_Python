from app_schooling.models.schooling_models import Schooling

from database.database import save
from database.database import commit
from database.database import db

def create(data:dict) -> Schooling:
    return save(
        Schooling(
            user_id = data['user_id'],
            grade = data['grade'],
            school_name = data['school_name'],
            course_name = data['course_name']
        )
    )

def get_schooling_by_id(schooling_id:int) -> Schooling:
    schooling = Schooling.query.filter_by(id_school=schooling_id).first()
    return schooling

def get_all_schooling() -> dict:
    all_schoolings = Schooling.query.all()
    return all_schoolings

def get_all_schoolings_from_one_user(id:int) -> dict:
    all_schoolings_user = Schooling.query.filter_by(user_id=id).first()
    return all_schoolings_user

def update_schooling(schooling_id:int,data_to_update:dict) -> Schooling:
    schooling_old = Schooling.query.get(schooling_id)
    schooling_old.grade = data_to_update['grade']
    schooling_old.school_name = data_to_update['school_name']
    schooling_old.course_name = data_to_update['course_name']
    commit()
    return schoolings_old

def delete_schooling(schooling_id:int) -> str:
    Schooling.query.filter_by(id=schooling_id).delete()
    commit()
    return "Escolaridade removida com sucesso." 