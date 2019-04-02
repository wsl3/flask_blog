from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


login_manager.login_view = "login"





from views import *
from admin import *
from models import Admin, Article, Tag, Info
from command import forge, admin
