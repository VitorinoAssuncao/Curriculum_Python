from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy import Date

from app_user.models.user_models import User

from database.database import save
from database.database import commit
from database.database import db

def create(data:dict) -> User:
    return save(
        User(
            login = data['login'],
            password = generate_password_hash(data['password']),
            name = data['name'],
            birth_date = data['birth_date']
        )
    )

def get_user_by_id(user_id:int) -> User:
    user = User.query.filter_by(id=user_id).first()
    return user

def get_all_user() -> dict:
    all_user = User.query.all()
    return all_user

def update_user(user_id:int,data_to_update:dict) -> User:
    user_old = User.query.get(user_id)
    user_old.login = data_to_update['login']
    user_old.password = generate_password_hash(data_to_update['password'])
    user_old.name = data_to_update['name']
    user_old.birth_date = data_to_update['birth_date']
    commit()
    return user_old

def delete_user(user_id:int) -> str:
    User.query.filter_by(id=user_id).delete()
    commit()
    return "Usuário removido com sucesso." 

def login(user_login:str,password:str) -> User:
    user = User.query.filter_by(login=user_login).first()
    if check_password_hash(user.password,password):
        return user
    else:
        return False

