from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)  # Init Flask-Migrate


    from app.routes import users, openai_api
    app.register_blueprint(users.bp)
    app.register_blueprint(openai_api.bp)

    return app