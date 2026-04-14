"""Tests TP1 — Héritage Personne / Etudiant / Cours.

Cycle TDD : ces tests sont écrits AVANT l'implémentation (phase RED),
puis les classes sont implémentées jusqu'à GREEN, puis refactorisées.
"""

import pytest

from cours import Cours
from etudiant import Etudiant
from personne import Personne


# ---------- Cours ----------
class TestCours:
    def test_creation_cours_valide(self):
        c = Cours("Mathématiques", "M. Dupont")
        assert c.nom_cours == "Mathématiques"
        assert c.professeur_responsable == "M. Dupont"

    def test_str_cours_contient_nom_et_prof(self):
        c = Cours("Physique", "Mme Curie")
        s = str(c)
        assert "Physique" in s
        assert "Curie" in s

    def test_cours_nom_vide_refuse(self):
        with pytest.raises(ValueError):
            Cours("", "M. Dupont")

    def test_cours_prof_vide_refuse(self):
        with pytest.raises(ValueError):
            Cours("Maths", "   ")


# ---------- Personne ----------
class TestPersonne:
    def test_creation_personne_valide(self):
        p = Personne("Alice", 25)
        assert p.nom == "Alice"
        assert p.age == 25

    def test_str_personne(self):
        p = Personne("Bob", 30)
        s = str(p)
        assert "Bob" in s
        assert "30" in s


# ---------- Etudiant : héritage ----------
class TestEtudiantHeritage:
    def test_etudiant_est_une_personne(self):
        e = Etudiant("Charlie", 20, "E001", 14.5)
        assert isinstance(e, Personne)
        assert isinstance(e, Etudiant)

    def test_etudiant_herite_attributs_personne(self):
        e = Etudiant("Charlie", 20, "E001", 14.5)
        assert e.nom == "Charlie"
        assert e.age == 20

    def test_etudiant_attributs_specifiques(self):
        e = Etudiant("Charlie", 20, "E001", 14.5)
        assert e.numero_etudiant == "E001"
        assert e.moyenne == 14.5
        assert e.liste_cours == []

    def test_ajouter_cours(self):
        e = Etudiant("Charlie", 20, "E001")
        c1 = Cours("Maths", "M. Dupont")
        c2 = Cours("Physique", "Mme Curie")
        e.ajouter_cours(c1)
        e.ajouter_cours(c2)
        assert len(e.liste_cours) == 2
        assert e.liste_cours[0].nom_cours == "Maths"

    def test_ajouter_cours_type_invalide_refuse(self):
        e = Etudiant("Charlie", 20, "E001")
        with pytest.raises(TypeError):
            e.ajouter_cours("Pas un cours")

    def test_str_etudiant_complet(self):
        e = Etudiant("Charlie", 20, "E001", 14.5)
        e.ajouter_cours(Cours("Maths", "M. Dupont"))
        s = str(e)
        assert "Charlie" in s
        assert "E001" in s
        assert "14" in s
        assert "Maths" in s
