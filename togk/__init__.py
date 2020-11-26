from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from decouple import config as config_decouple


def create_app(enviroment):
    app = Flask(__name__)  
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

# # Config
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "MYSECRET"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)

# Instances modules
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Routes
from togk import routes