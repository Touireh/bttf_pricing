from typing import List
from .models import Movie

# InputParser class to parse the input text
class InputParser:
    @staticmethod
    def parse(raw_text: str) -> List[Movie]:
        """
        Transforme une chaîne de caractères (avec retours à la ligne)
        en une liste d'objets Movie.
        """
        if not raw_text or not raw_text.strip():
            return []

        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        
        return [Movie(title=line) for line in lines]