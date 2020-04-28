from ..service.projection_service import *
from ..util.dto import ProjectionDto
from ..util.decorator import token_required, admin_token_required

from flask_restplus import Resource
from flask import request


api = ProjectionDto.api
_projection = ProjectionDto.projection


@api.route('/')
@api.param('date', 'Search by date')
class ProjectionList(Resource):
    @api.doc('List of projections')
    @api.marshal_list_with(_projection, envelope='data')
    def get(self):
        """List all projections"""
        return get_all_projections(request.args)

    @api.response(201, 'Projection successfully created.')
    @api.doc('create a new projection')
    @api.expect(_projection, validate=False)
    # @admin_token_required
    def post(self):
        """Creates a new Projection """
        data = request.json
        return save_new_projection(data=data)


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
