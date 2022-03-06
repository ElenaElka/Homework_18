from flask import request
from flask_restx import Resource, Namespace
from setup_db import db
from models import Movie, MovieSchema, FilterSchema
from marshmallow.exceptions import ValidationError

movie_ns = Namespace ('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:
            input_data = FilterSchema().load(request.args)
            movies = db.session.query(Movie).filter_by(**input_data).all()
            result = MovieSchema(many=True).dump(movies)
            return result, 200
        except ValidationError:
            return "", 400

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201

@movie_ns.route('/<int:pk>')
class MoviesView(Resource):
    def get(self, mid):
        movie = db.session.query(Movie).get(mid)
        if movie is not None:
            result = MovieSchema().dump(movie)
            return result, 200
        return "", 404

    def delete(self, mid: int):
        movie = Movie.query.get(mid)
        if movie is not None:
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        return "", 404

    def put(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404
        req_json = request.json
        movie.id = req_json.get("id")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204