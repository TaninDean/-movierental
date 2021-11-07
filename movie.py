class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__price_code = ''
        self.__year = year
        self.__genre = genre

    def get_price_code(self):
        return self.__price_code

    def set_price_code(self, value):
        self.__price_code = value

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def is_genre(self, genre):
        if genre in self.__genre:
            return True

    def __str__(self):
        return self.__title
