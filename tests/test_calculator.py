"""
Tests unitaires pour le calculateur de prix BTTF.
"""

import pytest
from src import PriceCalculator, InputParser, Movie
from src.models import BTTF_UNIT_PRICE, OTHER_UNIT_PRICE


class TestPriceCalculator:
    """Tests pour le calculateur de prix"""
    
    def test_example_1_three_different_bttf(self):
        """Exemple 1: 3 DVDs BTTF différents = 36€ (20% réduction)"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3")
        ]
        assert PriceCalculator.calculate_total(movies) == 36.0
    
    def test_example_2_two_different_bttf(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 3")
        ]
        assert PriceCalculator.calculate_total(movies) == 27.0
    
    def test_example_3_one_bttf(self):
        movies = [Movie("Back to the Future 1")]
        assert PriceCalculator.calculate_total(movies) == 15.0
    
    def test_example_4_duplicate_bttf(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("Back to the Future 2")  
        ]
        assert PriceCalculator.calculate_total(movies) == 48.0
    
    def test_example_5_bttf_and_other(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("La chèvre")
        ]
        assert PriceCalculator.calculate_total(movies) == 56.0
    
    def test_only_other_movies(self):
        movies = [
            Movie("La chèvre"),
            Movie("Les Visiteurs")
        ]
        assert PriceCalculator.calculate_total(movies) == 40.0
    
    def test_one_other_movie(self):
        movies = [Movie("La chèvre")]
        assert PriceCalculator.calculate_total(movies) == 20.0
    
    def test_mixed_movies_two_bttf(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("La chèvre")
        ]
        assert PriceCalculator.calculate_total(movies) == 47.0
    
    def test_mixed_movies_one_bttf(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("La chèvre"),
            Movie("Les Visiteurs")
        ]
        assert PriceCalculator.calculate_total(movies) == 55.0
    
    def test_many_duplicates_same_bttf(self):
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1")
        ]
        assert PriceCalculator.calculate_total(movies) == 45.0
    
    def test_many_other_movies(self):
        movies = [
            Movie("La chèvre"),
            Movie("Les Visiteurs"),
            Movie("Le Dîner de Cons"),
            Movie("Astérix et Obélix")
        ]
        assert PriceCalculator.calculate_total(movies) == 80.0
