from flask import Flask,render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql
from .config import config_by_name
# Flask 객체 인스턴스 생성
# 만일 static폴더를 지정하고 싶다면
# Flast(__name__,static_folder='./static')

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
# --------------------------------- [edit] ---------------------------------- #    
    app.config.from_object(config_by_name[config_name])
    # ORM
    # db.init_app(app)
    # migrate.init_app(app, db)
    from .views import auth,evaluate
    app.register_blueprint(auth.bp)
    app.register_blueprint(evaluate.bp)
    return app


