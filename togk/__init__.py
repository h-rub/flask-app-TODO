from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Instances modules
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Routes
from togk import routes