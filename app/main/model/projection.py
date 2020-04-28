import datetime
import jwt
from .. import db, flask_bcrypt
from ..config import key
from app.main.model.blacklist import BlacklistToken


class Projection(db.Model):
    """ Projection Model for storing projection related details """
    __tablename__ = "projection"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(16), nullable=False)
    cases = db.Column(db.Integer, nullable=False)
    leitos = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<Projection of type {} at {}: {} cases | {} leitos>".format(self.type, self.date, self.cases, self.leitos)
