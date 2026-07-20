"""La Boutique du Coin : calcul du montant d'une commande.

Regles metier (affichees sur le site) :
- Livraison a 4,90 EUR, OFFERTE a partir de 50 EUR d'achats (50 EUR inclus).
- Fidelite : 1 point = 1 % de remise, plafonnee a 30 % (nouvelle politique).
- La remise s'applique sur les articles, pas sur les frais de port.
- L'argent ne peut jamais devenir negatif : ni un total, ni une remise, ni un stock.
"""

FRAIS_DE_PORT = 4.90
PLAFOND_REMISE = 0.30  # 30 % : les gros clients meritent mieux (PixelForge)


def total_articles(panier):
    """Somme des articles du panier : liste de tuples (nom, prix, quantite)."""
    total = 0
    for nom, prix, quantite in panier:
        total = total + prix * quantite
    return total


def frais_de_port(total):
    # port offert a partir de 50 EUR d'achats, 50 EUR INCLUS (corrige au J8)
    if total >= 50:
        return 0.0
    return FRAIS_DE_PORT


def remise_fidelite(total, points):
    # 1 point = 1 % de remise, plafond releve par la nouvelle politique
    taux = min(points * 0.01, PLAFOND_REMISE)
    return total * taux


def total_commande(panier, points=0):
    """Montant final : articles - remise fidelite + frais de port."""
    t = total_articles(panier)
    r = remise_fidelite(t, points)
    return t - r + frais_de_port(t)
