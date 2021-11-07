# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from price import PriceCode
from movie_category import MovieCategory
from customer import Customer

def make_movies():
    cats = MovieCategory()
    movies = [
        cats.get_movie("The Irishman"),
        cats.get_movie("CitizenFour"),
        cats.get_movie("Frozen"),
        cats.get_movie("El Camino"),
        cats.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.for_movie(movie)))
        days += 1
    print(customer.statement())
