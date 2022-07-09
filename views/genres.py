from flask_restx import Namespace, Resource

from dao.model.genres import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = genre_service.get(genre_id)
        if genre:
            return genre_schema.dump(genre), 200
        return "", 404
