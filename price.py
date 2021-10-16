from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""

    new_release = {"price": lambda days: 3.0*days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2.0*days,
               "frp": lambda days: days
               }

    children = {"price": lambda days: 1.5*days,
                "frp": lambda days: days
                }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)
