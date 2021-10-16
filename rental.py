from price import PriceCode
from movie import Movie
import logging


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.rental_price()

    def rental_price(self):
        amount = 0
        if self.movie.get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 each.
            amount = 2.0
            if self.days_rented > 2:
                amount += PriceCode.regular.price(self.days_rented-2)
        elif self.movie.get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 each.
            amount = 1.5
            if self.days_rented > 3:
                amount += PriceCode.children.price(self.days_rented-3)
        elif self.movie.get_price_code() == Movie.NEW_RELEASE:
            # Straight per day charge
            amount += PriceCode.new_release.price(self.days_rented)
        else:
            log = logging.getLogger()
            log.error(
                f"Movie {self.movie} has unrecognized priceCode {self.movie.get_price_code()}")
        return amount

    def rental_points(self):
        frequent_renter_points = 0
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            frequent_renter_points += self.days_rented
        else:
            frequent_renter_points += 1
        return frequent_renter_points