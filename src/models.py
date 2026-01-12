from dataclasses import dataclass

BTTF_SAGA_NAME = "Back to the Future"
BTTF_UNIT_PRICE = 15.0
OTHER_UNIT_PRICE = 20.0

# Table des remises : {nombre_de_volets_differents: pourcentage_reduction}
DISCOUNT_RATES = {
    3: 0.20,
    2: 0.10,
    1: 0.00
}

@dataclass(frozen=True)
class Movie:
    title: str

    @property
    def is_bttf(self) -> bool:
        return BTTF_SAGA_NAME in self.title