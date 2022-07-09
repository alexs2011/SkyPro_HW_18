from dao.model.movies import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get(self, movie_id: int = None, **kwargs) -> list[Movie] | Movie:
        return self.dao.get(movie_id, **kwargs)

    def create(self, data) -> Movie:
        return self.dao.create(data)

    def update(self, movie_id, data) -> Movie | None:
        movie = self.dao.get(movie_id)
        if not movie:
            return None

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.dao.update(movie)
        return movie

    def update_partial(self, movie_id, data) -> Movie | None:
        movie = self.dao.get(movie_id)
        if not movie:
            return None

        if "title" in data:
            movie.title = data['title']
        if "description" in data:
            movie.description = data['description']
        if "trailer" in data:
            movie.trailer = data['trailer']
        if "year" in data:
            movie.year = data['year']
        if "rating" in data:
            movie.rating = data['rating']
        if "genre_id" in data:
            movie.genre_id = data['genre_id']
        if "director_id" in data:
            movie.director_id = data['director_id']

        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)
