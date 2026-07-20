# Conventions maison · La Boutique du Coin

Règles de revue de code de l'équipe. Un relecteur (humain ou agent) doit s'y tenir.

## Ce qui est BLOQUANT (sévérité haute)

1. **Un secret en dur dans le code** (clé d'API, mot de passe) : toujours bloquant, sans exception.
2. **Une entrée utilisateur qui part telle quelle dans une requête** (concaténation ou f-string dans du SQL) : bloquant.
3. **Une règle métier du site non respectée** (voir l'en-tête de `boutique.py` : port offert dès 50 EUR INCLUS, remise plafonnée à 20 %, stock jamais négatif) : bloquant.
4. **De l'argent qui peut devenir négatif** (total, remise, stock) : bloquant.

## Ce qui est IMPORTANT (sévérité moyenne)

5. Un cas limite non testé quand il touche à l'argent (frontières : 0, 50 EUR, plafonds).
6. Une fonction qui peut planter sur une entrée vide ou absente.
7. Un changement de comportement livré SANS le test qui le prouve.

## Ce dont on ne parle PAS en revue (bruit)

- Les `print()` de debug : tolérés en dev, le hook de pré-commit les enlève.
- Le style (noms de variables, longueur des lignes) : le formateur automatique s'en charge.
- Les suggestions de refactoring « pour faire joli » : hors sujet en revue.

## Format de verdict attendu

Pour chaque problème : `[SÉVÉRITÉ] fichier:ligne · le problème en une phrase · le correctif proposé en une phrase.`
Terminer par un verdict global : ACCEPTÉ ou REFUSÉ (refusé dès qu'il y a un bloquant).
