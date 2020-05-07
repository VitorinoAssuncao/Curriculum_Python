from database.database import db

class Schooling(db.Model):
    __tablename__ = 'schooling'
    id_school = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    grade = db.Column(db.String,nullable=False)
    school_name = db.Column(db.String,nullable=False)
    course_name = db.Column(db.String,nullable=False)   

    def __init__(self,**args):
        super(Schooling,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id_school' : self.id_school,
            'user_id': self.user_id,
            'grade': self.grade,
            'school_name': self.school_name,
            'course_name': self.course_name
        }