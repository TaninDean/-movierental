import unittest
from customer import Customer
from price import PriceCode
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan")
		self.regular_movie = Movie("CitizenFour")
		self.childrens_movie = Movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour")
		self.assertEqual("CitizenFour", m.get_title())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.new_release)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_charge(), 15.0)
		rental = Rental(self.regular_movie, 5, PriceCode.regular)
		self.assertEqual(rental.get_charge(), 6.5)
		rental = Rental(self.childrens_movie, 10, PriceCode.childrens)
		self.assertEqual(rental.get_charge(), 12.0)

	
	def test_rental_points(self):
		rental = Rental(self.regular_movie, 5.0, PriceCode.regular)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_rental_points(), 5)