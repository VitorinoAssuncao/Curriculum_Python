from database.database import db
from sqlalchemy import date

class Scholling(db.Model):
    __tablename__ = 'schooling'
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    name = db.Column(db.String,nullable=False)
    birth_date = db.Column(db.Date,nullable=False)