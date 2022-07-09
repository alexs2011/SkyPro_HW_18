from flask_restx import Namespace, Resource

from dao.model.directors import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id):
        director = director_service.get(director_id)
        if director:
            return director_schema.dump(director), 200
        return "", 404
