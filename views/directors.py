from flask_restx import Resource, Namespace
from setup_db import db
from models import Director, DirectorSchema

director_ns = Namespace ('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        i = db.session.query(Director).all()
        result = DirectorSchema(many=True).dump(i)
        return result, 200

@director_ns.route('/<int:pk>')
class DirectorsView(Resource):
    def get(self, did):
        director = db.session.query(Director).get(did)
        if director is not None:
            result = DirectorSchema().dump(director)
            return result, 200
        return "", 404
