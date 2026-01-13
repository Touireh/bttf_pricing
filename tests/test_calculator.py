"""
Tests unitaires pour le calculateur de prix BTTF.
Couvre tous les exemples du cahier des charges et les cas limites.
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
        # Calcul: 3 * 15€ = 45€, -20% = 36€
        assert PriceCalculator.calculate_total(movies) == 36.0
    
    def test_example_2_two_different_bttf(self):
        """Exemple 2: 2 DVDs BTTF différents = 27€ (10% réduction)"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 3")
        ]
        # Calcul: 2 * 15€ = 30€, -10% = 27€
        assert PriceCalculator.calculate_total(movies) == 27.0
    
    def test_example_3_one_bttf(self):
        """Exemple 3: 1 DVD BTTF = 15€ (pas de réduction)"""
        movies = [Movie("Back to the Future 1")]
        assert PriceCalculator.calculate_total(movies) == 15.0
    
    def test_example_4_duplicate_bttf(self):
        """Exemple 4: 4 DVDs dont 3 différents = 48€"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("Back to the Future 2")  # Doublon
        ]
        # Calcul: 4 * 15€ = 60€, -20% (car 3 différents) = 48€
        assert PriceCalculator.calculate_total(movies) == 48.0
    
    def test_example_5_bttf_and_other(self):
        """Exemple 5: 3 BTTF + 1 autre film = 56€"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("La chèvre")
        ]
        # Calcul: (3 * 15€ * 0.8) + 20€ = 36 + 20 = 56€
        assert PriceCalculator.calculate_total(movies) == 56.0
    
    def test_empty_basket(self):
        """Panier vide = 0€"""
        assert PriceCalculator.calculate_total([]) == 0.0
    
    def test_only_other_movies(self):
        """Seulement des films non-BTTF, pas de réduction"""
        movies = [
            Movie("La chèvre"),
            Movie("Les Visiteurs")
        ]
        # 2 * 20€ = 40€
        assert PriceCalculator.calculate_total(movies) == 40.0
    
    def test_one_other_movie(self):
        """Un seul film non-BTTF"""
        movies = [Movie("La chèvre")]
        assert PriceCalculator.calculate_total(movies) == 20.0
    
    def test_mixed_movies_two_bttf(self):
        """Mélange: 2 BTTF différents + 1 autre film"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("La chèvre")
        ]
        # BTTF: 2 * 15€ * 0.9 = 27€, Autre: 20€, Total: 47€
        assert PriceCalculator.calculate_total(movies) == 47.0
    
    def test_mixed_movies_one_bttf(self):
        """Mélange: 1 BTTF + 2 autres films"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("La chèvre"),
            Movie("Les Visiteurs")
        ]
        # BTTF: 15€ (pas de réduction), Autres: 40€, Total: 55€
        assert PriceCalculator.calculate_total(movies) == 55.0
    
    def test_many_duplicates_same_bttf(self):
        """Plusieurs copies du même DVD BTTF"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1")
        ]
        # 3 * 15€ = 45€, pas de réduction (1 seul volet différent)
        assert PriceCalculator.calculate_total(movies) == 45.0
    
    def test_many_other_movies(self):
        """Plusieurs films non-BTTF différents"""
        movies = [
            Movie("La chèvre"),
            Movie("Les Visiteurs"),
            Movie("Le Dîner de Cons"),
            Movie("Astérix et Obélix")
        ]
        # 4 * 20€ = 80€
        assert PriceCalculator.calculate_total(movies) == 80.0


class TestInputParser:
    """Tests pour le parser d'entrée"""
    
    def test_parse_single_line(self):
        """Parse une seule ligne"""
        result = InputParser.parse("Back to the Future 1")
        assert len(result) == 1
        assert result[0].title == "Back to the Future 1"
    
    def test_parse_multiple_lines(self):
        """Parse plusieurs lignes"""
        input_text = """Back to the Future 1
Back to the Future 2
La chèvre"""
        result = InputParser.parse(input_text)
        assert len(result) == 3
        assert result[0].title == "Back to the Future 1"
        assert result[1].title == "Back to the Future 2"
        assert result[2].title == "La chèvre"
    
    def test_parse_empty_string(self):
        """Parse chaîne vide"""
        assert InputParser.parse("") == []
    
    def test_parse_whitespace_only(self):
        """Parse chaîne avec seulement des espaces"""
        assert InputParser.parse("   \n\n   ") == []
    
    def test_parse_with_blank_lines(self):
        """Parse avec lignes vides intercalées"""
        input_text = """Back to the Future 1

Back to the Future 2

"""
        result = InputParser.parse(input_text)
        assert len(result) == 2
        assert result[0].title == "Back to the Future 1"
        assert result[1].title == "Back to the Future 2"
    
    def test_parse_strips_whitespace(self):
        """Parse nettoie les espaces en début et fin"""
        input_text = "  Back to the Future 1  \n  La chèvre  "
        result = InputParser.parse(input_text)
        assert result[0].title == "Back to the Future 1"
        assert result[1].title == "La chèvre"
    
    def test_parse_windows_line_endings(self):
        """Parse avec retours à la ligne Windows (CRLF)"""
        input_text = "Back to the Future 1\r\nBack to the Future 2"
        result = InputParser.parse(input_text)
        assert len(result) == 2
    
    def test_parse_unicode_characters(self):
        """Parse avec caractères Unicode"""
        input_text = "La chèvre\nL'Auberge espagnole\nAmélie Poulain"
        result = InputParser.parse(input_text)
        assert len(result) == 3
        assert result[0].title == "La chèvre"


class TestMovie:
    """Tests pour le modèle Movie"""
    
    def test_is_bttf_true_variant_1(self):
        """Détection BTTF - variante 1"""
        movie = Movie("Back to the Future 1")
        assert movie.is_bttf is True
    
    def test_is_bttf_true_variant_2(self):
        """Détection BTTF - variante 2"""
        movie = Movie("Back to the Future 2")
        assert movie.is_bttf is True
    
    def test_is_bttf_true_variant_3(self):
        """Détection BTTF - variante 3"""
        movie = Movie("Back to the Future 3")
        assert movie.is_bttf is True
    
    def test_is_bttf_false(self):
        """Détection non-BTTF"""
        movie = Movie("La chèvre")
        assert movie.is_bttf is False
    
    def test_is_bttf_case_sensitive(self):
        """Détection BTTF est sensible à la casse"""
        # Avec la casse différente, ce ne devrait pas être détecté comme BTTF
        movie = Movie("back to the future 1")
        assert movie.is_bttf is False
    
    def test_immutability(self):
        """Movie est immutable (frozen dataclass)"""
        movie = Movie("Back to the Future 1")
        with pytest.raises(Exception):  # FrozenInstanceError
            movie.title = "New title"
    
    def test_equality(self):
        """Deux movies avec le même titre sont égaux"""
        movie1 = Movie("Back to the Future 1")
        movie2 = Movie("Back to the Future 1")
        assert movie1 == movie2
    
    def test_inequality(self):
        """Deux movies avec des titres différents ne sont pas égaux"""
        movie1 = Movie("Back to the Future 1")
        movie2 = Movie("Back to the Future 2")
        assert movie1 != movie2
    
    def test_hashable(self):
        """Movie est hashable (peut être utilisé dans un set)"""
        movie1 = Movie("Back to the Future 1")
        movie2 = Movie("Back to the Future 1")
        movie3 = Movie("Back to the Future 2")
        
        unique_movies = {movie1, movie2, movie3}
        assert len(unique_movies) == 2  # movie1 et movie2 sont identiques


class TestIntegration:
    """Tests d'intégration bout-en-bout"""
    
    def test_full_workflow_example_1(self):
        """Test complet: parsing + calcul pour exemple 1"""
        input_text = """Back to the Future 1
Back to the Future 2
Back to the Future 3"""
        
        basket = InputParser.parse(input_text)
        total = PriceCalculator.calculate_total(basket)
        
        assert total == 36.0
    
    def test_full_workflow_example_5(self):
        """Test complet: parsing + calcul pour exemple 5"""
        input_text = """Back to the Future 1
Back to the Future 2
Back to the Future 3
La chèvre"""
        
        basket = InputParser.parse(input_text)
        total = PriceCalculator.calculate_total(basket)
        
        assert total == 56.0
    
    def test_full_workflow_with_blank_lines(self):
        """Test complet avec lignes vides"""
        input_text = """
Back to the Future 1

Back to the Future 2

"""
        
        basket = InputParser.parse(input_text)
        total = PriceCalculator.calculate_total(basket)
        
        assert total == 27.0
    
    def test_full_workflow_empty_input(self):
        """Test complet avec entrée vide"""
        basket = InputParser.parse("")
        total = PriceCalculator.calculate_total(basket)
        
        assert total == 0.0


class TestDiscountLogic:
    """Tests spécifiques à la logique de réduction"""
    
    def test_no_discount_for_one_unique(self):
        """Pas de réduction avec 1 seul volet unique"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1"),
            Movie("Back to the Future 1")
        ]
        total = PriceCalculator.calculate_total(movies)
        # 3 * 15 = 45, pas de réduction
        assert total == 45.0
    
    def test_ten_percent_discount_for_two_unique(self):
        """10% de réduction avec 2 volets uniques"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2")
        ]
        total = PriceCalculator.calculate_total(movies)
        # 2 * 15 = 30, -10% = 27
        assert total == 27.0
    
    def test_twenty_percent_discount_for_three_unique(self):
        """20% de réduction avec 3 volets uniques"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3")
        ]
        total = PriceCalculator.calculate_total(movies)
        # 3 * 15 = 45, -20% = 36
        assert total == 36.0
    
    def test_discount_applies_to_all_bttf_items(self):
        """La réduction s'applique à TOUS les DVDs BTTF, même les doublons"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("Back to the Future 1"),  # Doublon
            Movie("Back to the Future 2")   # Doublon
        ]
        total = PriceCalculator.calculate_total(movies)
        # 5 * 15 = 75, -20% (car 3 uniques) = 60
        assert total == 60.0
    
    def test_discount_not_applied_to_other_movies(self):
        """La réduction ne s'applique PAS aux autres films"""
        movies = [
            Movie("Back to the Future 1"),
            Movie("Back to the Future 2"),
            Movie("Back to the Future 3"),
            Movie("La chèvre"),
            Movie("Les Visiteurs")
        ]
        total = PriceCalculator.calculate_total(movies)
        # BTTF: 3 * 15 * 0.8 = 36
        # Autres: 2 * 20 = 40
        # Total: 76
        assert total == 76.0
