# La Boutique du Coin · en ligne

Le logiciel de caisse de la Boutique du Coin (articles, frais de port, fidélité, stock, clients), assaini lors de la grande revue du J8 : les règles métier sont dans l'en-tête de `boutique.py`, la loi de revue dans `CONVENTIONS.md`, et chaque bug corrigé a laissé son test dans `test_boutique.py`.

Ce repo est gardé par des robots (dossier `.github/workflows/`) :

- **la garde** : les tests tournent à chaque push et sur chaque Pull Request ;
- **le relecteur** : un agent relit chaque Pull Request et poste son verdict en commentaire ;
- **le veilleur** : chaque nuit à 3h, un agent fait sa ronde et ouvre son rapport dans une issue.

Règle de la maison : **les robots proposent, l'humain merge.**

## Lancer les tests à la main

```
python -m pytest -v
```
