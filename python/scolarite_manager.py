"""Module ScolariteManager — Patterns SINGLETON + OBSERVER.

Pattern Singleton : une seule instance de ScolariteManager dans toute l'application.
    → Centralise la liste globale des étudiants et les statistiques.

Pattern Observer : ScolariteManager implémente l'interface Observer.
    → Quand la moyenne d'un étudiant change, il est notifié automatiquement
      et recalcule les statistiques globales.

SRP : gère uniquement le registre global des étudiants et leurs statistiques.
OCP : ouvert à l'extension (on peut ajouter d'autres statistiques sans modifier
      le mécanisme d'observation).
DIP : dépend de l'abstraction Observer, pas d'une implémentation concrète.
"""

from __future__ import annotations

from typing import List, Optional

from etudiant import Etudiant, Observer


class ScolariteManager(Observer):
    """Gestionnaire unique (Singleton) de la scolarité.

    Usage :
        manager = ScolariteManager.get_instance()
        manager.ajouter_etudiant(etudiant)
    """

    _instance: Optional["ScolariteManager"] = None

    # ----- Singleton -----
    def __new__(cls) -> "ScolariteManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialise = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialise:
            return
        self.__etudiants: List[Etudiant] = []
        self.__moyenne_globale: float = 0.0
        self._initialise = True

    @classmethod
    def get_instance(cls) -> "ScolariteManager":
        """Point d'accès global au singleton."""
        return cls()

    @classmethod
    def reset_instance(cls) -> None:
        """Utilitaire de test — détruit le singleton pour repartir à zéro."""
        cls._instance = None

    # ----- Gestion des étudiants -----
    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        if not isinstance(etudiant, Etudiant):
            raise TypeError("Seul un Etudiant peut être ajouté.")
        self.__etudiants.append(etudiant)
        # L'étudiant enregistre le manager comme observateur
        etudiant.ajouter_observer(self)
        self._recalculer_statistiques()

    def retirer_etudiant(self, etudiant: Etudiant) -> None:
        self.__etudiants.remove(etudiant)
        etudiant.retirer_observer(self)
        self._recalculer_statistiques()

    @property
    def etudiants(self) -> List[Etudiant]:
        return list(self.__etudiants)

    @property
    def moyenne_globale(self) -> float:
        return self.__moyenne_globale

    @property
    def nombre_etudiants(self) -> int:
        return len(self.__etudiants)

    # ----- Pattern Observer : callback -----
    def mise_a_jour(self, etudiant: Etudiant) -> None:
        """Appelée automatiquement quand la moyenne d'un étudiant change."""
        print(
            f"  [Observer] Notification reçue : {etudiant.nom} → "
            f"nouvelle moyenne = {etudiant.moyenne:.2f}"
        )
        self._recalculer_statistiques()

    # ----- Statistiques -----
    def _recalculer_statistiques(self) -> None:
        if not self.__etudiants:
            self.__moyenne_globale = 0.0
            return
        total = sum(e.moyenne for e in self.__etudiants)
        self.__moyenne_globale = total / len(self.__etudiants)

    def afficher_statistiques(self) -> str:
        return (
            f"=== Statistiques Scolarité ===\n"
            f"Nombre d'étudiants : {len(self.__etudiants)}\n"
            f"Moyenne globale    : {self.__moyenne_globale:.2f}/20"
        )

    def __repr__(self) -> str:
        return (
            f"ScolariteManager(nb_etudiants={len(self.__etudiants)}, "
            f"moyenne_globale={self.__moyenne_globale:.2f})"
        )
