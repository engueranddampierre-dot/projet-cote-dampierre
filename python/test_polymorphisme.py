"""Tests TP3 — Polymorphisme via afficher_details().

Vérifie :
- afficher_details() définie dans Personne et redéfinie dans Etudiant et Enseignant,
- une liste hétérogène list[Personne] traite les éléments uniformément
  SANS recourir à isinstance / type() dans la boucle (LSP + OCP).
"""

from typing import List

from enseignant import Enseignant
from etudiant import Etudiant
from personne import Personne


class TestPolymorphisme:
    def test_personne_afficher_details(self):
        p = Personne("Alice", 30)
        details = p.afficher_details()
        assert "Alice" in details
        assert "30" in details

    def test_etudiant_override_afficher_details(self):
        e = Etudiant("Bob", 22, "E042", 15.5)
        details = e.afficher_details()
        assert "Bob" in details
        assert "Étudiant" in details or "Etudiant" in details
        assert "15" in details
        assert "E042" in details

    def test_enseignant_override_afficher_details(self):
        ens = Enseignant("Mme Curie", 45, "Physique", 3500.0)
        details = ens.afficher_details()
        assert "Curie" in details
        assert "Enseignant" in details
        assert "Physique" in details
        assert "3500" in details

    def test_liste_heterogene_polymorphe(self):
        """Le test clé : une boucle générique sur une liste de Personne.

        Aucun isinstance, aucun type() dans la boucle — c'est le polymorphisme
        qui dispatche au bon afficher_details() selon le type réel.
        """
        liste: List[Personne] = [
            Etudiant("Alice", 20, "E001", 14.0),
            Enseignant("M. Dupont", 50, "Maths", 4000.0),
            Etudiant("Bob", 22, "E002", 16.5),
            Personne("Visiteur", 35),
        ]

        resultats = [p.afficher_details() for p in liste]

        # Chaque résultat a la signature de son type réel
        assert "Étudiant" in resultats[0] or "Etudiant" in resultats[0]
        assert "Enseignant" in resultats[1]
        assert "Étudiant" in resultats[2] or "Etudiant" in resultats[2]
        # Personne : pas de préfixe spécifique
        assert "Visiteur" in resultats[3]

    def test_lsp_substituabilite(self):
        """LSP : Etudiant et Enseignant sont substituables à Personne."""

        def afficher_anonyme(p: Personne) -> str:
            # Cette fonction ne sait pas quel type concret elle reçoit.
            # Elle DOIT fonctionner pour toute Personne ou sous-classe.
            return p.afficher_details()

        # Aucune doit lever d'exception (contrat respecté)
        assert afficher_anonyme(Personne("X", 20))
        assert afficher_anonyme(Etudiant("Y", 21, "E1", 10.0))
        assert afficher_anonyme(Enseignant("Z", 40, "Info", 3000.0))


# ---------- Validation Enseignant (cohérence TP2 + TP3) ----------
class TestEnseignantValidation:
    def test_salaire_negatif_refuse(self):
        import pytest
        with pytest.raises(ValueError):
            Enseignant("X", 40, "Maths", -100.0)

    def test_matiere_vide_refuse(self):
        import pytest
        with pytest.raises(ValueError):
            Enseignant("X", 40, "", 3000.0)
