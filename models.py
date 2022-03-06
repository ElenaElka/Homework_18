from marshmallow import Schema, fields
from setup_db import db


class Movie(db.Model):
     __tablename__ = 'movie'
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String)
     description = db.Column(db.String)
     trailer = db.Column(db.String)
     year = db.Column(db.Integer)
     rating = db.Column(db.Integer)
     director_id = db.Column(db.Integer)
     genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
     director_id = db.Column(db.Integer, db.ForeignKey("genre.id"))

class MovieSchema(Schema):
     id = fields.Int()
     title = fields.String()
     description = fields.String()
     trailer = fields.String()
     year = fields.Integer()
     rating = fields.Integer()
     director_id = fields.Integer()
     genre_id = fields.Integer()
     director_id = fields.Integer()

class FilterSchema(Schema):
     director_id = fields.Int(required=False)
     genre_id = fields.Int(required=False)
     year = fields.Int(required=False)


class Director(db.Model):
     __tablename__ = 'directror'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)

class DirectorSchema(Schema):
     id = fields.Int()
     name = fields.Str()


class Genre(db.Model):
     __tablename__ = 'genre'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)

class GenreSchema(Schema):
     id = fields.Int()
     name = fields.Str()