# Gestion Étudiante — Module 1 (ENSTA Brest / Institut Polytechnique de Paris)

TP fil-rouge **Ingénierie Logicielle — Module 1** implémenté en **Python** et en **Java**, avec une démarche **TDD stricte** (RED → GREEN → REFACTOR) et application des principes **SOLID** du Module 2.

> **Périmètre** : les trois TP enchaînés — Héritage, Encapsulation, Polymorphisme — sur le même fil rouge `Personne / Etudiant / Enseignant / Cours`.

---

## 📁 Structure du dépôt

```
gestion-etudiante/
├── README.md
├── .gitignore
├── docs/
│   └── uml.md                       # Diagramme UML PlantUML
├── python/
│   ├── cours.py
│   ├── personne.py
│   ├── etudiant.py
│   ├── enseignant.py
│   ├── main.py                      # Démo TP1
│   ├── main_tp2.py                  # Démo TP2
│   ├── main_tp3.py                  # Démo TP3
│   ├── test_heritage.py             # 14 tests
│   ├── test_encapsulation.py        # 17 tests
│   ├── test_polymorphisme.py        # 7 tests
│   └── requirements.txt
└── java/
    ├── pom.xml
    └── src/
        ├── main/java/com/ensta/gestion/
        │   ├── Cours.java
        │   ├── Personne.java
        │   ├── Etudiant.java
        │   ├── Enseignant.java
        │   ├── Main.java
        │   ├── MainTp2.java
        │   └── MainTp3.java
        └── test/java/com/ensta/gestion/
            ├── TestHeritage.java
            ├── TestEncapsulation.java
            └── TestPolymorphisme.java
```

---

## 🚀 Lancement rapide

### Python

```bash
cd python
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt

# Exécuter les démos
python main.py        # TP1 — Héritage
python main_tp2.py    # TP2 — Encapsulation
python main_tp3.py    # TP3 — Polymorphisme

# Tous les tests (38 tests)
pytest -v

# Par TP
pytest test_heritage.py -v
pytest test_encapsulation.py -v
pytest test_polymorphisme.py -v

# Couverture
pytest --cov=. --cov-report=html
```

### Java

```bash
cd java

# Tous les tests
mvn test

# Par TP
mvn test -Dtest=TestHeritage
mvn test -Dtest=TestEncapsulation
mvn test -Dtest=TestPolymorphisme

# Exécuter les démos
mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.Main
mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.MainTp2
mvn compile exec:java -Dexec.mainClass=com.ensta.gestion.MainTp3

# Alternative sans Maven (javac + java)
mkdir -p target/classes
javac -d target/classes src/main/java/com/ensta/gestion/*.java
java -cp target/classes com.ensta.gestion.Main
```

---

## 🧭 Les trois TP

### TP1 — Héritage (Réutilisation)

Trois classes qui reflètent la relation **« est-un »** :

- `Cours` : nom du cours + professeur responsable.
- `Personne` (mère) : nom, âge.
- `Etudiant` (fille) hérite de `Personne` et ajoute : numéro étudiant, moyenne, liste de cours.

Points clés :
- `super().__init__(...)` / `super(...)` obligatoire en première instruction du constructeur enfant.
- `isinstance(etudiant, Personne)` / `assertInstanceOf(Personne.class, etudiant)` vérifient le lien d'héritage.
- `__str__` / `toString()` complets avec délégation au parent via `super()`.

### TP2 — Encapsulation (Sécurité)

Tous les attributs deviennent **privés** et sont accessibles uniquement via getters/setters validés :

| Règle métier                               | Exception levée                         |
| ------------------------------------------ | --------------------------------------- |
| `age` ∈ [0, 100]                           | `ValueError` / `IllegalArgumentException` |
| `moyenne` ∈ [0.0, 20.0]                    | idem                                    |
| `nom` non vide, non blanc, non nul         | idem                                    |
| `numero_etudiant` **lecture seule** après création | pas de setter exposé             |
| `liste_cours` accessible via `ajouter_cours()` uniquement (copie défensive) | — |

Preuve : les tests du TP1 restent 100 % verts après l'ajout de l'encapsulation.

### TP3 — Polymorphisme (Flexibilité)

- `afficher_details()` / `afficherDetails()` est définie dans `Personne` et **redéfinie (override)** dans `Etudiant` et `Enseignant`.
- `Enseignant` ajoute `matiere` et `salaire` (avec validation).
- Le `main_tp3` parcourt une `list[Personne]` / `List<Personne>` **hétérogène** et appelle la même méthode sur chaque élément — la liaison dynamique dispatche automatiquement.
- **Aucun `isinstance` / `instanceof` dans la boucle** — c'est la garantie LSP + OCP.

---

## ✅ Application des principes SOLID (Module 2)

| Principe | Application dans ce TP |
| -------- | ---------------------- |
| **S — Single Responsibility** | Chaque classe a une seule responsabilité : `Cours` = données d'un cours ; `Personne` = identité ; `Etudiant` = identité académique ; `Enseignant` = identité enseignante. Aucune classe ne fait à la fois logique + persistance + affichage. |
| **O — Open / Closed** | Ajouter un nouveau type de personne (`Doctorant`, `PersonnelAdministratif`…) se fait via une nouvelle classe qui hérite de `Personne` et redéfinit `afficher_details()`. Zéro modification du code existant, zéro `if/elif` sur le type. |
| **L — Liskov Substitution** | `Etudiant` et `Enseignant` sont strictement substituables à `Personne` : `afficher_details()` retourne toujours une `str`/`String` non vide et **ne lève jamais d'exception**. La fonction `afficher_anonyme(p: Personne)` fonctionne pour tout sous-type (test dédié). |
| **I — Interface Segregation** | Pas d'interface monolithique forcée. Si on voulait découpler, on introduirait `IAffichable` (contenant juste `afficher_details`) sans polluer les classes de données. |
| **D — Dependency Inversion** | La conception est préparée : la classe `Etudiant` ne dépend pas d'une source de données concrète. Pour TP suivants (SOLID Module 2), on injectera un `IRepo` via constructeur sans toucher à la logique métier. |

---

## 🧪 Cycle TDD appliqué

Pour chaque TP :

1. **RED** — on écrit d'abord les tests (`test_*.py` / `TestX.java`). Ils échouent car les classes / méthodes n'existent pas encore.
2. **GREEN** — on écrit le code minimal pour faire passer les tests.
3. **REFACTOR** — on nettoie, on factorise (passage par setters dans constructeurs, copie défensive, constantes `AGE_MIN`/`MOYENNE_MAX`, etc.) sans casser les tests.

Résultat : **38 tests Python** et **30 tests Java** (3 fichiers × TP × nested classes). Tous verts.

---

## 📊 Diagramme UML

Voir [`docs/uml.md`](docs/uml.md).

```
          Personne
          /       \
    Etudiant   Enseignant

    Etudiant *── Cours  (composition : un étudiant possède 0..* cours)
```

---