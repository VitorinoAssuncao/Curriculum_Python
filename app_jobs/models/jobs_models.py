from database.database import db
from sqlalchemy import Date

class Jobs(db.Model):
    __tablename__ = 'jobs'
    id_job = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    function = db.Column (db.String,nullable=False)
    enterprise = db.Column (db.String,nullable=False)
    date_begin = db.Column (db.Date,nullable=False)
    date_out = db.Column (db.Date,nullable=False)
    activities = db.Column (db.String,nullable=True)

    def __init__(self,**args):
        super(Jobs,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            "id_job" : self.id_job,
            "user_id" : self.user_id,
            "function" : self.function,
            "enterprise" : self.enterprise,
            "date_begin" : self.date_begin,
            "date_out" : self.date_out,
            "activities" : self.activities
        }