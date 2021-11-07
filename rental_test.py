import unittest
from customer import Customer
from price import PriceCode
from rental import Rental
from movie import Movie
from movie_category import MovieCategory


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.category_movie = MovieCategory()
        self.new_movie = self.category_movie.get_movie("Mulan")
        self.regular_movie = self.category_movie.get_movie("A Tenant")
        self.childrens_movie = self.category_movie.get_movie(
            "The Legend of Sarila")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = self.category_movie.get_movie("Mulan")
        self.assertEqual("Mulan", m.get_title())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_charge(), 4.5)
        rental = Rental(self.regular_movie, 5,
                        PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_charge(), 6.5)
        rental = Rental(self.childrens_movie, 10,
                        PriceCode.for_movie(self.childrens_movie))
        self.assertEqual(rental.get_charge(), 12.0)

    def test_rental_points(self):
        rental = Rental(self.regular_movie, 5.0,
                        PriceCode.for_movie(self.regular_movie))
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
        self.assertEqual(rental.get_rental_points(), 1)
