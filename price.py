from enum import Enum
from datetime import datetime
from movie_category import MovieCategory

class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""

    new_release = {"price": lambda days: 3.0*days,
                   "frp": lambda days: days,
                   }
    regular = {"price": lambda days: 2 + 1.5*(days-2) if days > 2 else 2,
               "frp": lambda days: 1,
               }

    childrens = {"price": lambda days: 1.5 + 1.5*(days-3) if days > 3 else 1.5,
                "frp": lambda days: 1,
                }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def frequent_rental_points(self, days: int):
        """Return the rental point for a given number of day"""
        freq = self.value['frp']
        return freq(days)

    @staticmethod
    def for_movie(movie):
        if movie.get_year() == str(datetime.now().year):
            return PriceCode.new_release
        if 'Children' in movie.get_genre():
            return PriceCode.childrens
        return PriceCode.regular
