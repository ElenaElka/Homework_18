from flask_restx import Resource, Namespace
from setup_db import db
from models import Genre, GenreSchema

genre_ns = Namespace ('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        i = db.session.query(Genre).all()
        result = GenreSchema(many=True).dump(i)
        return result, 200


@genre_ns.route('/<int:pk>')
class GenresView(Resource):
    def get(self, gid):
        genre = db.session.query(Genre).get(gid)
        if genre is not None:
            result = GenreSchema().dump(genre)
            return result, 200
        return "", 404
