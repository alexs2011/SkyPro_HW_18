from dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, director_id=None):
        """
        Получение информации из бд. Если director_id задан, то извлекается информация о режиссёре с этим id,
        иначе - обо всех режиссёрах.
        """
        if director_id:
            return self.session.query(Director).filter(Director.id == director_id).first()
        return self.session.query(Director).all()
