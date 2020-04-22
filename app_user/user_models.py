from database.database import db
from sqlalchemy import Date

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    name = db.Column(db.String,nullable=False)
    birth_date = db.Column(db.Date,nullable=False)

    def __init__(self,**args):
        super(User,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.id,
            'login': self.login,
            'password':self.password,
            'name' : self.name,
            'birth_date':self.birth_date
        }