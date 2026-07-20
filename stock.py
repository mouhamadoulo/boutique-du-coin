"""Gestion du stock de la Boutique du Coin.

Regle metier : on ne peut jamais vendre plus que le stock disponible.
"""

stock = {
    "mug": 12,
    "tee-shirt": 30,
    "casquette": 5,
}


def _verifier_quantite(quantite):
    """Une quantite doit etre un entier strictement positif."""
    if quantite <= 0:
        raise ValueError("quantite invalide")


def disponible(article):
    """Nombre d'exemplaires en rayon pour cet article (0 si inconnu)."""
    return stock.get(article, 0)


def retirer(article, quantite):
    """Retire des articles du stock apres une vente.

    Refuse la vente si le stock ne suffit pas : le rayon ne peut
    jamais passer en negatif (regle metier, verifiee par les tests).
    """
    _verifier_quantite(quantite)
    if quantite > disponible(article):
        raise ValueError("stock insuffisant pour " + article)
    stock[article] = stock[article] - quantite
    return stock[article]


def reapprovisionner(article, quantite):
    """Ajoute des articles au stock a la reception d'une livraison."""
    _verifier_quantite(quantite)
    stock[article] = stock.get(article, 0) + quantite
    return stock[article]
