import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrasp import Bootstrap
from flas_login import LoginManager
from flask_bcrypt import Bcrypt

db= SQLAlchemy()
bootstrap = Bootstrap()
bcrypt= Bcrypt()
login_manager = LoginManager()
login_manager.login_view="authenticacion.log"
login_manager.session_proteccion= "strong"

def create_app(config_type):
    app= Flask(__name__)
    configuration = os.path.join(os.getcwd(), "config", config_type+".py")
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init.app(app)
    login_manager.init.app(app)
    bcrypt.init.app(app)
    from app.auth import authentication
    app.register_blueprint(authentication)
    return app