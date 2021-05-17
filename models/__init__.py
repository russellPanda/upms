from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    return db
    # db.create_all()
    # from .permission import User,Role,Ability
    # db.drop_all()
    # db.create_all()
    # db.session.commit()
