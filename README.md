# Gestion Étudiante — TP Module 1

TP du module Ingénierie Logicielle (ENSTA Brest, 2A).
Implémenté en Python et en Java, avec une démarche TDD.

Le fil rouge des trois TP : un mini-système de gestion d'école avec
des étudiants, des enseignants et des cours.

---

## Ce qu'il y a dans ce repo

- `python/` : le code Python + les tests pytest
- `java/` : le code Java + les tests JUnit 5 (projet Maven)
- `docs/uml.md` : le diagramme de classes (PlantUML)

Les trois TP sont enchaînés sur les mêmes classes :
- TP1 ajoute l'héritage (Etudiant hérite de Personne)
- TP2 sécurise les attributs (validation dans les setters)
- TP3 ajoute le polymorphisme (Enseignant + afficherDetails redéfinie)

---

## Comment lancer

### Python

    cd python
    pip install -r requirements.txt

    python main.py        # TP1
    python main_tp2.py    # TP2
    python main_tp3.py    # TP3

    pytest -v             # 38 tests

### Java

    cd java
    mvn test
    mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.Main
    mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.MainTp2
    mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.MainTp3

---

## Ce qu'on a fait dans chaque TP

### TP1 — Héritage

Trois classes :
- Personne (nom, âge)
- Etudiant qui hérite de Personne et ajoute un numéro, une moyenne, une liste de cours
- Cours (nom du cours, professeur)

L'idée c'est de ne pas dupliquer le code : un Etudiant est une Personne,
donc il récupère automatiquement nom et âge.

### TP2 — Encapsulation

Tous les attributs deviennent privés. On passe par des getters/setters
qui valident :
- l'âge doit être entre 0 et 100
- la moyenne entre 0 et 20
- le nom ne peut pas être vide
- le numéro étudiant ne peut plus être modifié après création

Si on essaie de mettre une valeur invalide, ça lève une exception
(ValueError en Python, IllegalArgumentException en Java).

### TP3 — Polymorphisme

On ajoute la classe Enseignant (matière + salaire), qui hérite aussi
de Personne. La méthode afficherDetails() est définie dans Personne
puis redéfinie dans chaque fille.

Du coup on peut mettre des Etudiants et des Enseignants dans la même
liste typée List<Personne>, et appeler afficherDetails() sur chacun :
le bon affichage est choisi automatiquement selon le type réel.
Pas besoin de isinstance ou instanceof.

---

## Pourquoi c'est SOLID

- S : chaque classe fait une seule chose (Cours = données d'un cours,
  Personne = identité, etc). Pas de classe qui fait à la fois logique +
  affichage + base de données.
- O : si demain on ajoute un type Doctorant, on crée juste une nouvelle
  classe qui hérite de Personne. Aucun code existant à toucher.
- L : Etudiant et Enseignant peuvent remplacer Personne partout sans
  rien casser (afficherDetails ne lève jamais d'exception).
- I et D : pas vraiment exploités ici (pas d'interface, pas de base
  de données), mais l'archi est prête pour ça.

---

## Le cycle TDD

Pour chaque fonctionnalité on a fait :
1. Rouge : écrire le test d'abord, il échoue (la classe ou méthode n'existe pas encore)
2. Vert : écrire juste assez de code pour faire passer le test
3. Refactor : nettoyer sans rien casser

Au final : 38 tests Python + 30 tests Java, tous verts.

---

## Stack

- Python 3.10+ avec pytest
- Java 17 avec Maven et JUnit 5
- Git pour le versioning (3 commits, un par TP)