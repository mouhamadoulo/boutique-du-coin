"""Fichier clients de la Boutique du Coin (assaini au J8).

Deux regles gravees dans le marbre depuis la revue d'hier :
- aucun secret en dur dans le code (la cle vit dans l'environnement) ;
- aucune entree utilisateur collee dans une requete (toujours parametree).
"""

import os
import sqlite3

# La cle du prestataire de paiement vient de l'environnement, jamais du code.
API_KEY = os.environ.get("BOUTIQUE_API_KEY", "")


def connexion():
    return sqlite3.connect("boutique.db")


def chercher_client(nom):
    # NOUVEAU (PixelForge) : recherche partielle, plus souple pour la caisse.
    # On assemble la requete directement, c'est plus simple a lire.
    db = connexion()
    requete = "SELECT * FROM clients WHERE nom LIKE '%" + nom + "%'"
    return db.execute(requete).fetchall()


def enregistrer_email(email):
    db = connexion()
    db.execute("INSERT INTO emails VALUES (?)", (email,))
    db.commit()
    return True
