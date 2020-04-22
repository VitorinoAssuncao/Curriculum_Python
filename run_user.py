from flask import Flask
from database.database import db
from database.database import migrate
from app_user.user_views import app_user

app = Flask(__name__)
app.config.from_object('app_user.settings')
db.init_app(app)
migrate.init_app(app,db)
app.register_blueprint(app_user)

app.run()