"""Module Decorator — Pattern DECORATOR pour Etudiant.

Permet d'ajouter dynamiquement des responsabilités à un objet Etudiant
SANS modifier la classe Etudiant originale.

Exemples :
    - EtudiantBoursier  : ajoute le montant de la bourse à l'affichage.
    - EtudiantDelegue   : ajoute le rôle de délégué de promotion.

OCP : on peut créer de nouveaux décorateurs (EtudiantSportif, EtudiantErasmus…)
      sans toucher aux classes existantes.
LSP : chaque décorateur est substituable à Etudiant grâce à la délégation
      transparente de toutes les propriétés.
"""

from __future__ import annotations

from typing import List

from cours import Cours
from etudiant import Etudiant, Observer


# ---------------------------------------------------------------------------
# Décorateur de base (classe abstraite)
# ---------------------------------------------------------------------------
class EtudiantDecorator(Etudiant):
    """Décorateur abstrait : enveloppe un Etudiant et délègue les appels.

    Hérite d'Etudiant pour respecter le typage (isinstance), mais
    redirige tout vers l'étudiant enveloppé (_etudiant).
    """

    def __init__(self, etudiant: Etudiant):
        # On n'appelle PAS super().__init__() pour éviter de créer
        # un second jeu d'attributs. On délègue tout à _etudiant.
        object.__init__(self)
        self._etudiant = etudiant

    # ----- Délégation transparente des propriétés -----
    @property
    def nom(self) -> str:
        return self._etudiant.nom

    @nom.setter
    def nom(self, valeur: str) -> None:
        self._etudiant.nom = valeur

    @property
    def age(self) -> int:
        return self._etudiant.age

    @age.setter
    def age(self, valeur: int) -> None:
        self._etudiant.age = valeur

    @property
    def numero_etudiant(self) -> str:
        return self._etudiant.numero_etudiant

    @property
    def moyenne(self) -> float:
        return self._etudiant.moyenne

    @moyenne.setter
    def moyenne(self, valeur: float) -> None:
        self._etudiant.moyenne = valeur

    @property
    def liste_cours(self) -> List[Cours]:
        return self._etudiant.liste_cours

    def ajouter_cours(self, cours: Cours) -> None:
        self._etudiant.ajouter_cours(cours)

    def ajouter_observer(self, obs: Observer) -> None:
        self._etudiant.ajouter_observer(obs)

    def retirer_observer(self, obs: Observer) -> None:
        self._etudiant.retirer_observer(obs)

    # ----- Méthode décorée (point d'extension) -----
    def afficher_details(self) -> str:
        return self._etudiant.afficher_details()

    def __str__(self) -> str:
        return self.afficher_details()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._etudiant!r})"


# ---------------------------------------------------------------------------
# Décorateur concret : EtudiantBoursier
# ---------------------------------------------------------------------------
class EtudiantBoursier(EtudiantDecorator):
    """Ajoute les informations de bourse à un Etudiant."""

    def __init__(self, etudiant: Etudiant, montant_bourse: float):
        super().__init__(etudiant)
        if montant_bourse < 0:
            raise ValueError("Le montant de la bourse ne peut pas être négatif.")
        self.__montant_bourse = montant_bourse

    @property
    def montant_bourse(self) -> float:
        return self.__montant_bourse

    def afficher_details(self) -> str:
        base = self._etudiant.afficher_details()
        return f"{base} | 🎓 Boursier ({self.__montant_bourse:.2f} €/an)"


# ---------------------------------------------------------------------------
# Décorateur concret : EtudiantDelegue
# ---------------------------------------------------------------------------
class EtudiantDelegue(EtudiantDecorator):
    """Ajoute le rôle de délégué de promotion à un Etudiant."""

    def __init__(self, etudiant: Etudiant, promotion: str = ""):
        super().__init__(etudiant)
        self.__promotion = promotion.strip() if promotion else "sa promotion"

    @property
    def promotion(self) -> str:
        return self.__promotion

    def afficher_details(self) -> str:
        base = self._etudiant.afficher_details()
        return f"{base} | 📋 Délégué de {self.__promotion}"
