"""
Ce fichier permet de savoir si une chaîne de charactère est un palindrome ou non.
"""

import re  # Pour obtenir les expressions régulières
import unicodedata  # Pour manipuler les caractères Unicode, ici pour retirer les accents

def ispalindrome(p):
    """
    Cette fonction renvoie un booléen pour savoir si p est un palindrome
    """
    # Supprimer tous les accents
    mot_sans_accents = ''.join(
        c for c in unicodedata.normalize('NFD', p)
        if unicodedata.category(c) != 'Mn'
    )
    # Supprimer les caractères spéciaux et les espaces et mettre en minuscule
    mot_filtre = re.sub(r'[^a-zA-Z0-9]', '', mot_sans_accents).lower()
    # Vérifier si la chaîne filtrée est un palindrome
    return mot_filtre == mot_filtre[::-1]


#### Fonction principale

def main():
    """
    Le main qui permet d'éxecuter le programme avec des valeurs différentes pour p
    """

    # vos appels à la fonction secondaire ici

    for s in ["Radar", "kayak", "lévél", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
