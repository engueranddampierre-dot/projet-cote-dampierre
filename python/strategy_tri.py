"""Module Strategy — Pattern STRATEGY pour le tri / calcul de mention.

Définit une famille d'algorithmes interchangeables (tri par moyenne,
tri par nom, calcul de mention) encapsulés derrière une interface commune.

Le code client choisit dynamiquement la stratégie à utiliser, sans modifier
la logique de tri elle-même.

OCP : ajouter une nouvelle stratégie = créer une nouvelle classe, zéro
      modification du code existant.
DIP : le code client dépend de l'abstraction StrategyTri, pas des implémentations.
SRP : chaque stratégie n'a qu'une seule responsabilité.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from etudiant import Etudiant


# ---------------------------------------------------------------------------
# Interface Strategy
# ---------------------------------------------------------------------------
class StrategyTri(ABC):
    """Interface abstraite pour les stratégies de tri d'étudiants."""

    @abstractmethod
    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        """Retourne une nouvelle liste triée (ne modifie pas l'originale)."""

    @abstractmethod
    def description(self) -> str:
        """Nom lisible de la stratégie."""


# ---------------------------------------------------------------------------
# Stratégie concrète : tri par moyenne (décroissant)
# ---------------------------------------------------------------------------
class TriParMoyenne(StrategyTri):
    """Trie les étudiants par moyenne décroissante."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.moyenne, reverse=True)

    def description(self) -> str:
        return "Tri par moyenne (décroissant)"


# ---------------------------------------------------------------------------
# Stratégie concrète : tri par nom (alphabétique)
# ---------------------------------------------------------------------------
class TriParNom(StrategyTri):
    """Trie les étudiants par nom alphabétique."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.nom.lower())

    def description(self) -> str:
        return "Tri par nom (alphabétique)"


# ---------------------------------------------------------------------------
# Stratégie concrète : calcul de mention
# ---------------------------------------------------------------------------
class MentionStrategy(StrategyTri):
    """Trie les étudiants par mention (Très Bien > Bien > AB > Passable > Échec)."""

    MENTIONS = {
        "Très Bien": 4,
        "Bien": 3,
        "Assez Bien": 2,
        "Passable": 1,
        "Insuffisant": 0,
    }

    @staticmethod
    def calculer_mention(moyenne: float) -> str:
        if moyenne >= 16:
            return "Très Bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez Bien"
        elif moyenne >= 10:
            return "Passable"
        else:
            return "Insuffisant"

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(
            etudiants,
            key=lambda e: self.MENTIONS.get(
                self.calculer_mention(e.moyenne), 0
            ),
            reverse=True,
        )

    def description(self) -> str:
        return "Tri par mention"


# ---------------------------------------------------------------------------
# Contexte : utilise une stratégie de manière interchangeable
# ---------------------------------------------------------------------------
class ContexteTri:
    """Contexte qui utilise une StrategyTri pour trier une liste d'étudiants.

    La stratégie peut être changée dynamiquement à tout moment.

    Usage :
        ctx = ContexteTri(TriParMoyenne())
        resultat = ctx.executer(liste_etudiants)
        ctx.set_strategy(TriParNom())
        resultat = ctx.executer(liste_etudiants)
    """

    def __init__(self, strategy: StrategyTri):
        self.__strategy = strategy

    def set_strategy(self, strategy: StrategyTri) -> None:
        """Change dynamiquement la stratégie de tri."""
        self.__strategy = strategy

    def executer(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        """Exécute la stratégie courante et retourne la liste triée."""
        print(f"  [Strategy] {self.__strategy.description()}")
        return self.__strategy.trier(etudiants)
