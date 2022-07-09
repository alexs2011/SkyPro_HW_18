from dao.director import DirectorDAO
from dao.model.directors import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get(self, director_id: int = None) -> list[Director] | Director:
        return self.dao.get(director_id)
