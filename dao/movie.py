from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, movie_id=None, **kwargs):
        """
        Получение информации из бд. Если movie_id задан, то извлекается информация о фильме с этим id, иначе - обо всех
        фильмах. В kwargs содержатся опциональные параметры фильтрации.
        """
        # Подготавливаем запрос
        query = self.session.query(Movie)

        if movie_id:
            return query.filter(Movie.id == movie_id).first()

        # Последовательно применяем к запросу параметры фильтрации.
        if kwargs:
            for key, val in kwargs.items():
                query = query.filter(eval(f"Movie.{key}") == int(val))

        return query.all()

    def create(self, data):
        """
        Создание нового фильма в бд.
        """
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, data):
        """
        Обновление информации о фильме в бд.
        """
        self.session.add(data)
        self.session.commit()
        self.session.close()

    def delete(self, movie_id):
        """
        Удаление фильма из бд.
        """
        movie = self.get(movie_id)
        if not movie:
            return None
        self.session.delete(movie)
        self.session.commit()
