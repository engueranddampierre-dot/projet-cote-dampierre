"""Module Cours — Représente un cours académique.

SRP : cette classe a une seule responsabilité — représenter un cours
(nom + professeur responsable). Aucune logique d'affichage métier,
aucune persistance, aucune notification.
"""


class Cours:
    """Un cours académique avec un nom et un professeur responsable."""

    def __init__(self, nom_cours: str, professeur_responsable: str):
        if not nom_cours or not nom_cours.strip():
            raise ValueError("Le nom du cours ne peut pas être vide.")
        if not professeur_responsable or not professeur_responsable.strip():
            raise ValueError("Le professeur responsable ne peut pas être vide.")
        self.__nom_cours = nom_cours.strip()
        self.__professeur_responsable = professeur_responsable.strip()

    @property
    def nom_cours(self) -> str:
        return self.__nom_cours

    @property
    def professeur_responsable(self) -> str:
        return self.__professeur_responsable

    def __str__(self) -> str:
        return f"{self.__nom_cours} (Prof : {self.__professeur_responsable})"

    def __repr__(self) -> str:
        return f"Cours(nom_cours={self.__nom_cours!r}, professeur={self.__professeur_responsable!r})"
