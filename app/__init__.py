# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.projection_controller import api as projection_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Projections API',
          version='1.0',
          description='API for Corona Vairus Projections built with Flask RESTPlus and JWT'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(projection_ns, path='/projection')
api.add_namespace(auth_ns)
