from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier', read_only=True)
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ProjectionDto:
    api = Namespace('projection', description='projection related operations')
    projection = api.model('projection', {
        'id': fields.String(readonly=True, description='Projection id'),
        'type': fields.String(required=True, description='Projection type'),
        'date': fields.Date(required=True, description='Projection date'),
        'cases': fields.Integer(required=True, description='Projected cases on date'),
        'leitos': fields.Integer(required=True, description='Projected leitos on date'),
    })
