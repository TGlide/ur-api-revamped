from ..service.projection_service import *
from ..util.dto import ProjectionDto
from ..util.decorator import token_required, admin_token_required

from flask_restplus import Resource
from flask import request


api = ProjectionDto.api
_projection = ProjectionDto.projection


@api.route('/city')
@api.param('date', 'Search by date')
class CityProjectionList(Resource):
    @api.marshal_list_with(_projection, envelope='data')
    def get(self):
        """List all city projections"""
        return get_all_projections(request.args, 'city')

    @api.response(201, 'Projection successfully created.')
    @api.expect(_projection, validate=False)
    # @admin_token_required
    def post(self):
        """Creates a new city Projection """
        data = request.json
        return save_new_projection(data=data, type='city')


@api.route('/state')
@api.param('date', 'Search by date')
class StateProjectionList(Resource):
    @api.marshal_list_with(_projection, envelope='data')
    def get(self):
        """List all state projections"""
        return get_all_projections(request.args, 'state')

    @api.response(201, 'Projection successfully created.')
    @api.expect(_projection, validate=False)
    # @admin_token_required
    def post(self):
        """Creates a new state Projection """
        data = request.json
        return save_new_projection(data=data, type='state')


@api.route('/<id>')
@api.param('id', 'The Projection identifier')
@api.response(404, 'Projection not found.')
class Projection(Resource):
    @api.doc('get a projection')
    @api.marshal_with(_projection)
    def get(self, id):
        """get a projection given its identifier"""
        projection = get_a_projection(id)
        if not projection:
            api.abort(404)
        else:
            return projection

    @api.doc('delete a projection')
    def delete(self, id):
        """delete a projection given its identifier"""
        projection = get_a_projection(id)
        if not projection:
            api.abort(404)
        else:
            return delete_a_projection(projection)
