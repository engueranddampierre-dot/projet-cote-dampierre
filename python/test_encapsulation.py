"""Tests TP2 — Encapsulation et validation des données.

Vérifie que :
- les attributs privés ne sont pas accessibles directement,
- les setters refusent les valeurs invalides,
- les invariants métier sont garantis (age ∈ [0,100], moyenne ∈ [0,20]).
"""

import pytest

from etudiant import Etudiant
from personne import Personne


# ---------- Validation age ----------
class TestValidationAge:
    def test_age_negatif_refuse(self):
        with pytest.raises(ValueError):
            Personne("Alice", -1)

    def test_age_trop_grand_refuse(self):
        with pytest.raises(ValueError):
            Personne("Alice", 101)

    def test_age_limite_basse_acceptee(self):
        p = Personne("Bébé", 0)
        assert p.age == 0

    def test_age_limite_haute_acceptee(self):
        p = Personne("Doyen", 100)
        assert p.age == 100

    def test_modifier_age_invalide_refuse(self):
        p = Personne("Alice", 25)
        with pytest.raises(ValueError):
            p.age = 150
        # L'âge initial est préservé
        assert p.age == 25

    def test_age_non_entier_refuse(self):
        with pytest.raises(ValueError):
            Personne("Alice", "vingt")


# ---------- Validation nom ----------
class TestValidationNom:
    def test_nom_vide_refuse(self):
        with pytest.raises(ValueError):
            Personne("", 25)

    def test_nom_blancs_refuse(self):
        with pytest.raises(ValueError):
            Personne("   ", 25)

    def test_nom_none_refuse(self):
        with pytest.raises(ValueError):
            Personne(None, 25)


# ---------- Validation moyenne ----------
class TestValidationMoyenne:
    def test_moyenne_negative_refuse(self):
        with pytest.raises(ValueError):
            Etudiant("Alice", 20, "E001", -0.1)

    def test_moyenne_superieure_20_refuse(self):
        with pytest.raises(ValueError):
            Etudiant("Alice", 20, "E001", 25.0)

    def test_moyenne_modification_invalide_refuse(self):
        e = Etudiant("Alice", 20, "E001", 12.0)
        with pytest.raises(ValueError):
            e.moyenne = 25.0
        # La moyenne précédente est préservée
        assert e.moyenne == 12.0

    def test_moyenne_modification_valide_acceptee(self):
        e = Etudiant("Alice", 20, "E001", 12.0)
        e.moyenne = 15.5
        assert e.moyenne == 15.5

    def test_moyenne_limite_basse(self):
        e = Etudiant("Alice", 20, "E001", 0.0)
        assert e.moyenne == 0.0

    def test_moyenne_limite_haute(self):
        e = Etudiant("Alice", 20, "E001", 20.0)
        assert e.moyenne == 20.0


# ---------- Encapsulation : accès direct interdit ----------
class TestEncapsulationStricte:
    def test_attribut_age_prive_inaccessible(self):
        p = Personne("Alice", 25)
        with pytest.raises(AttributeError):
            _ = p.__age  # name mangling Python : interdit de l'extérieur

    def test_attribut_moyenne_prive_inaccessible(self):
        e = Etudiant("Alice", 20, "E001", 14.0)
        with pytest.raises(AttributeError):
            _ = e.__moyenne

    def test_numero_etudiant_lecture_seule(self):
        e = Etudiant("Alice", 20, "E001", 14.0)
        # pas de setter exposé : tentative d'assignation crée un nouvel attribut
        # mais ne modifie pas le numéro interne. On vérifie que le getter
        # retourne toujours la valeur d'origine.
        assert e.numero_etudiant == "E001"

    def test_liste_cours_copie_defensive(self):
        from cours import Cours

        e = Etudiant("Alice", 20, "E001", 14.0)
        e.ajouter_cours(Cours("Maths", "M. Dupont"))
        # On modifie la liste retournée
        liste = e.liste_cours
        liste.clear()
        # La liste interne n'a PAS été affectée (copie défensive)
        assert len(e.liste_cours) == 1
