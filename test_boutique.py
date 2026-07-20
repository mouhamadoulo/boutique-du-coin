"""Tests de la boutique, renforces au J8 : chaque bug d'hier a laisse son test."""

import pytest

from boutique import total_articles, frais_de_port, remise_fidelite, total_commande
from stock import disponible, retirer, reapprovisionner


def test_total_articles():
    panier = [("mug", 10.0, 2), ("tee-shirt", 15.0, 1)]
    assert total_articles(panier) == 35.0


def test_port_paye_sous_50():
    assert frais_de_port(35.0) == 4.90


def test_port_offert_au_dessus_de_50():
    assert frais_de_port(80.0) == 0.0


def test_port_offert_a_50_exactement():
    # la frontiere corrigee au J8 : 50 EUR inclus, comme promis sur le site
    assert frais_de_port(50.0) == 0.0


def test_remise_10_points():
    assert remise_fidelite(100.0, 10) == 10.0


def test_remise_plafonnee_a_20_pour_cent():
    # le bug des 150 points, corrige au J8 : jamais plus de 20 %
    assert remise_fidelite(100.0, 150) == 20.0


def test_commande_simple():
    panier = [("casquette", 20.0, 1)]
    assert total_commande(panier) == 24.90


def test_commande_jamais_negative():
    panier = [("casquette", 20.0, 1)]
    assert total_commande(panier, points=150) >= 0


def test_stock_refuse_de_passer_negatif():
    # le bug du stock, corrige au J8 : impossible de vendre ce qu'on n'a pas
    with pytest.raises(ValueError):
        retirer("casquette", 999)


def test_vente_normale_decremente_le_stock():
    avant = disponible("mug")
    retirer("mug", 2)
    assert disponible("mug") == avant - 2
    reapprovisionner("mug", 2)
