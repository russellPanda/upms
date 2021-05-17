from flask import Flask
from upms.config import config
from flask_debugtoolbar import DebugToolbarExtension
from flask_debug_api import DebugAPIExtension

def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])
    app.config['SECRET_KEY'] = 'Onceas#11'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config.from_object()

    from upms import models,routes
    models.init_app(app)
    routes.init_app(app)
    DebugToolbarExtension(app)
    DebugAPIExtension(app)
    app.debug = True
    panels = list(app.config['DEBUG_TB_PANELS'])
    panels.append('flask_debug_api.BrowseAPIPanel')
    app.config['DEBUG_TB_PANELS']=panels
    app.config['DEBUG_API_PREFIX'] = '/todos'

    return app


