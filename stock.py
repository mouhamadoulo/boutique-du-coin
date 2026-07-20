"""Gestion du stock de la Boutique du Coin.

Regle metier : on ne peut jamais vendre plus que le stock disponible.
"""

stock = {
    "mug": 12,
    "tee-shirt": 30,
    "casquette": 5,
}


def disponible(article):
    return stock.get(article, 0)


def retirer(article, quantite):
    """Retire des articles du stock apres une vente (verifications ajoutees au J8)."""
    if quantite <= 0:
        raise ValueError("quantite invalide")
    if quantite > disponible(article):
        raise ValueError("stock insuffisant pour " + article)
    stock[article] = stock[article] - quantite
    return stock[article]


def reapprovisionner(article, quantite):
    if quantite <= 0:
        raise ValueError("quantite invalide")
    stock[article] = stock.get(article, 0) + quantite
    return stock[article]
