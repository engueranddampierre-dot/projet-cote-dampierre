"""Module Etudiant — Hérite de Personne.

TP1 : héritage (super().__init__) + ajoute numero_etudiant, moyenne, liste_cours.
TP2 : encapsulation moyenne + numero_etudiant en lecture seule + liste_cours protégée.
TP3 : afficher_details() override polymorphe.
TP4 : Pattern Observer — Etudiant est le *Sujet Observable*.
      Quand la moyenne est modifiée, tous les observateurs enregistrés sont notifiés.

SRP : Etudiant représente l'identité académique d'un étudiant.
LSP : substituable à Personne — afficher_details() retourne une str, ne lève rien.
OCP : le mécanisme d'observation est ouvert à l'extension (n'importe quel Observer
      peut s'abonner) sans modifier la classe.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from cours import Cours
from personne import Personne


# ---------------------------------------------------------------------------
# Pattern OBSERVER — interface Observer (DIP : dépendance vers l'abstraction)
# ---------------------------------------------------------------------------
class Observer(ABC):
    """Interface observateur : reçoit les mises à jour d'un Etudiant."""

    @abstractmethod
    def mise_a_jour(self, etudiant: "Etudiant") -> None:
        """Appelée automatiquement quand la moyenne d'un étudiant change."""


# ---------------------------------------------------------------------------
# Classe Etudiant (Sujet Observable)
# ---------------------------------------------------------------------------
class Etudiant(Personne):
    """Un étudiant : une Personne avec un numéro, une moyenne et des cours."""

    MOYENNE_MIN = 0.0
    MOYENNE_MAX = 20.0

    def __init__(
        self,
        nom: str,
        age: int,
        numero_etudiant: str,
        moyenne: float = 0.0,
    ):
        super().__init__(nom, age)
        if not numero_etudiant or not str(numero_etudiant).strip():
            raise ValueError("Le numéro d'étudiant ne peut pas être vide.")
        self.__numero_etudiant = str(numero_etudiant).strip()
        self.__liste_cours: List[Cours] = []
        self.__observers: List[Observer] = []
        # passage par le setter pour validation (ne notifie pas encore car
        # _notifier vérifie que des observers existent)
        self.moyenne = moyenne

    # ----- Observer : abonnement / désabonnement -----
    def ajouter_observer(self, obs: Observer) -> None:
        if obs not in self.__observers:
            self.__observers.append(obs)

    def retirer_observer(self, obs: Observer) -> None:
        self.__observers.remove(obs)

    def _notifier(self) -> None:
        for obs in self.__observers:
            obs.mise_a_jour(self)

    # ----- numero_etudiant : lecture seule -----
    @property
    def numero_etudiant(self) -> str:
        return self.__numero_etudiant

    # ----- moyenne : encapsulée + validée + notification -----
    @property
    def moyenne(self) -> float:
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, valeur: float) -> None:
        if not isinstance(valeur, (int, float)) or isinstance(valeur, bool):
            raise ValueError("La moyenne doit être un nombre.")
        if valeur < self.MOYENNE_MIN or valeur > self.MOYENNE_MAX:
            raise ValueError(
                f"La moyenne doit être comprise entre {self.MOYENNE_MIN} et "
                f"{self.MOYENNE_MAX} (reçu : {valeur})."
            )
        self.__moyenne = float(valeur)
        # Notification automatique des observateurs (Pattern Observer)
        self._notifier()

    # ----- liste_cours : accès contrôlé -----
    @property
    def liste_cours(self) -> List[Cours]:
        return list(self.__liste_cours)

    def ajouter_cours(self, cours: Cours) -> None:
        if not isinstance(cours, Cours):
            raise TypeError("ajouter_cours attend une instance de Cours.")
        self.__liste_cours.append(cours)

    # ----- polymorphisme TP3 -----
    def afficher_details(self) -> str:
        base = super().afficher_details()
        cours_txt = (
            ", ".join(c.nom_cours for c in self.__liste_cours)
            if self.__liste_cours
            else "aucun cours"
        )
        return (
            f"[Étudiant] {base} | N° {self.__numero_etudiant} | "
            f"Moyenne : {self.__moyenne:.2f}/20 | Cours : {cours_txt}"
        )

    def __repr__(self) -> str:
        return (
            f"Etudiant(nom={self.nom!r}, age={self.age}, "
            f"numero={self.__numero_etudiant!r}, moyenne={self.__moyenne})"
        )
