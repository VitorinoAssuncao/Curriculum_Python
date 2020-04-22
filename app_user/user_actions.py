from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy import Date

from app_user.user_models import User
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

def login(user_login:str,password:str) -> User:
    user = User.query.filter_by(login=user_login).first()
    if check_password_hash(user.password,password):
        return user
    else:
        return False

def get_user_by_id(user_id:int) -> User:
    user = User.query.filter_by(id=user_id).first()
    return user

def get_all_user() -> dict:
    all_user = User.query.all()
    return all_user
