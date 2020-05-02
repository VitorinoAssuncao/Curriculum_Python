from flask import Flask
from database.database import db
from database.database import migrate
from app_user.views.user_views import app_user
from app_jobs.views.jobs_views import app_jobs

app = Flask(__name__)
app.config.from_object('app_user.settings')
db.init_app(app)
migrate.init_app(app,db)

app.register_blueprint(app_user)
app.register_blueprint(app_jobs)

app.run()