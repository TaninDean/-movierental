class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).

    def __init__(self, title):
        # Initialize a new movie.
        self.title = title
        self.__price_code = None

    def get_price_code(self):
        return self.__price_code

    def set_price_code(self, value):
        self.__price_code = value

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
