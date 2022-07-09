from flask import make_response, request
from flask_restx import Namespace, Resource

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get(**request.args)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.create(req_json)

        resp = make_response("", 201)
        resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = movie_service.get(movie_id)
        if movie:
            return movie_schema.dump(movie), 200
        return "", 404

    def put(self, movie_id):
        req_json = request.json
        updated_movie = movie_service.update(movie_id, req_json)
        if updated_movie:
            return movie_schema.dump(updated_movie), 204
        return "", 404

    def patch(self, movie_id):
        req_json = request.json
        updated_movie = movie_service.update_partial(movie_id, req_json)
        if updated_movie:
            return movie_schema.dump(updated_movie), 204
        return "", 404

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return "", 204
