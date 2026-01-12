from typing import List
from .models import Movie, BTTF_UNIT_PRICE, OTHER_UNIT_PRICE, DISCOUNT_RATES

class PriceCalculator:
    @staticmethod
    def calculate_total(movies: List[Movie]) -> float:
        bttf_movies = [m for m in movies if m.is_bttf]
        other_movies = [m for m in movies if not m.is_bttf]

        # Calcul pour la saga Back to the Future
        bttf_total = PriceCalculator._calculate_bttf_subtotal(bttf_movies)
        
        # Calcul pour les autres films
        others_total = len(other_movies) * OTHER_UNIT_PRICE

        return bttf_total + others_total

    @staticmethod
    def _calculate_bttf_subtotal(movies: List[Movie]) -> float:
        if not movies:
            return 0.0

        # Identifier le nombre de volets uniques (1, 2, 3...)
        unique_titles = {m.title for m in movies}
        nb_unique = len(unique_titles)

        # Déterminer le taux de remise applicable selon les règles
        # On prend la remise la plus haute possible par rapport au nombre d'uniques
        applicable_discount = 0.0
        for threshold in sorted(DISCOUNT_RATES.keys(), reverse=True):
            if nb_unique >= threshold:
                applicable_discount = DISCOUNT_RATES[threshold]
                break

        base_price = len(movies) * BTTF_UNIT_PRICE
        return base_price * (1 - applicable_discount)