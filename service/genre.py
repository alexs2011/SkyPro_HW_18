from dao.genre import GenreDAO
from dao.model.genres import Genre


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get(self, genre_id: int = None) -> list[Genre] | Genre:
        return self.dao.get(genre_id)
