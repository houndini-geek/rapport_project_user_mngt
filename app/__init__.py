from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()
DATABASE_URI = os.environ['RAPPORT_PROJECT_URI']


def create_app():
    app =  Flask(__name__)

    app.config['SECRET_KEY'] = 'mustbechangedforprod!'
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://postgres:%40ElonMusk@localhost:5432/rapport_project'
    )

    db.init_app(app)


    from app.routes import register_routes
    register_routes(app)

    return app