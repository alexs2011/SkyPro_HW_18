from dao.model.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, genre_id=None):
        """
        Получение информации из бд. Если genre_id задан, то извлекается информация о жанре с этим id, иначе - обо всех
        жанрах.
        """
        if genre_id:
            return self.session.query(Genre).filter(Genre.id == genre_id).first()
        return self.session.query(Genre).all()
