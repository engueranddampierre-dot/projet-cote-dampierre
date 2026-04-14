"""Module Etudiant — Hérite de Personne.

TP1 : héritage (super().__init__) + ajoute numero_etudiant, moyenne, liste_cours.
TP2 : encapsulation moyenne + numero_etudiant en lecture seule + liste_cours protégée.
TP3 : afficher_details() override polymorphe.

SRP : Etudiant représente l'identité académique d'un étudiant.
LSP : substituable à Personne — afficher_details() retourne une str, ne lève rien.
"""

from typing import List

from cours import Cours
from personne import Personne


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
        # numero_etudiant : lecture seule après création (pas de setter exposé)
        self.__numero_etudiant = str(numero_etudiant).strip()
        self.__liste_cours: List[Cours] = []
        # passage par le setter pour validation
        self.moyenne = moyenne

    # ----- numero_etudiant : lecture seule -----
    @property
    def numero_etudiant(self) -> str:
        return self.__numero_etudiant

    # ----- moyenne : encapsulée + validée -----
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

    # ----- liste_cours : accès contrôlé -----
    @property
    def liste_cours(self) -> List[Cours]:
        # On retourne une copie défensive : impossible de modifier la liste interne
        # depuis l'extérieur. Encapsulation respectée.
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
