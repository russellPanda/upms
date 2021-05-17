from .user import user_bp
from .test import index_bp


def init_app(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(index_bp)

