from flask import Flask
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('configurationFile.py')

db = SQLAlchemy(app)
from modelsFile import User, Role

login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
