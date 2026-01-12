import sys
from src import InputParser, PriceCalculator

def main():
    """
    Lit l'entrée standard, calcule le prix et affiche le résultat.
    """
    print("Veuillez entrer les titres des films dans le panier, un par ligne. Terminez par Ctrl+D (Linux/Mac) ou Ctrl+Z (Windows).")
    input_data = sys.stdin.read().strip()
    
    if not input_data:
        print(0)
        return

    basket = InputParser.parse(input_data)

    # Calcul
    total = PriceCalculator.calculate_total(basket)

    # On affiche un entier si le résultat est rond, sinon un float
    print("Prix total : ", end="")
    print(int(total) if total.is_integer() else total)

if __name__ == "__main__":
    main()