import sys
from src import InputParser, PriceCalculator

def main():
    if sys.stdin.isatty():
        print("Veuillez entrer les titres des films dans le panier, un par ligne. Terminez par Ctrl+Z (Windows) puis Entrée.", file=sys.stderr)

    input_data = sys.stdin.read().strip()
    
    if not input_data:
        print(0)
        return

    basket = InputParser.parse(input_data)

    # Calculate total price
    total = PriceCalculator.calculate_total(basket)

    # Print total price
    print(int(total) if total.is_integer() else total)

if __name__ == "__main__":
    main()