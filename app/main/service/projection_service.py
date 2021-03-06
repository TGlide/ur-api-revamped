import uuid
import datetime
import requests

from app.main import db
from app.main.model.projection import Projection

from sqlalchemy import func, or_,  nullslast, desc, asc


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def save_new_projection(data, type):
    projection = Projection.query.filter_by(
        date=data['date'], type=type).first()
    if not projection:
        try:
            new_projection = Projection(
                date=data['date'],
                type=type,
                cases=data.get('cases', 0),
                leitos=data.get('leitos', 0),
            )
            save_changes(new_projection)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        except:
            response_object = {
                'status': 'fail',
                'message': 'API error fuck :(',
            }
            return response_object, 409
    else:
        try:
            projection.date = data['date'],
            projection.type = type,
            projection.cases = data.get('cases', projection.cases),
            projection.leitos = data.get('leitos', projection.leitos)

            db.session.commit()

            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        except:
            response_object = {
                'status': 'fail',
                'message': 'API error fuck :(',
            }
            return response_object, 409


def delete_a_projection(projection):
    try:
        db.session.delete(projection)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.'
        }
        return response_object, 200
    except:
        response_object = {
            'status': 'fail',
            'message': f'Failed to delete projection.'
        }
        return response_object, 404


def get_all_projections(args, type):
    projections = Projection.query.filter_by(type=type)

    date = args.get('date', None)

    if date:
        projections = projections.filter(func.lower(Projection.date).contains(func.lower(
            date)))

    return projections.all()


def get_a_projection(id):
    return Projection.query.filter_by(id=id).first()
