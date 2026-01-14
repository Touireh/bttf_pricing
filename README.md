# Back to the Future Pricing Calculator

Ce projet implémente un calculateur de prix pour une boutique de DVD, avec des règles de promotion spécifiques pour la saga "Back to the Future".

## Règles de Prix

- **Prix de base** :
  - "Back to the Future" (tous les volets) : 15 €
  - Autres films : 20 €

- **Promotions (uniquement sur les titres "Back to the Future")** :
  - 2 volets *différents* achetés : **-10%** sur l'ensemble des BTTF.
  - 3 volets *différents* achetés : **-20%** sur l'ensemble des BTTF.

## Prérequis

- Python 3.10 ou supérieur.

## Installation

Installez les dépendances (pour les tests) :

```bash
pip install -r requirements.txt
```

## Utilisation

Le programme lit les titres de films depuis l'entrée standard (stdin) et affiche le prix total sur la sortie standard (stdout).

### Windows

Vous pouvez utiliser le script `run.bat` pour lancer le programme facilement :

```bat
run.bat
```

Ou manuellement via PowerShell :

```powershell
python main.py
```

Entrez les films ligne par ligne, puis faites `Ctrl+Z` et `Entrée` pour terminer la saisie.

### Linux / macOS

```bash
python main.py
```

Entrez les films ligne par ligne, puis faites `Ctrl+D` pour terminer.

### Exemple via pipe

```bash
echo "Back to the Future 1" | python main.py
# Sortie: 15
```

## Développement & Tests

Pour lancer les tests unitaires :

```bash
pytest
```
