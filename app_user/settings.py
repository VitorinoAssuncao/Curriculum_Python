import os
FLASK_APP = 'run'
MYSQL_DATABASE_USER = "desenvolvedor"
MYSQL_DATABASE_PASSWORD = "teste_user"
MYSQL_DATABASE_DB = "chega_mais"
MYSQL_DATABASE_HOST = "localhost"
MYSQL_DATABASE_PORT = "3306"
SERVER_HOST_NAME = "localhost"
SQLALCHEMY_DATABASE_URI = os.path.join('mysql+pymysql://desenvolvedor:teste_user@localhost:3306/chega_mais')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',True)

HOST = 'localhost'
PORT = '5000'
DEBUG = True
SECRET_KEY = 'chega_mais'