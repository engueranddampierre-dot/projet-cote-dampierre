"""Module Personne — Classe mère du système de gestion étudiante.

TP1 : structure de base + héritage.
TP2 : encapsulation — attributs privés + validation via setters.
TP3 : afficher_details() = méthode polymorphe (redéfinie dans les sous-classes).

SRP : Personne représente uniquement l'identité d'un individu (nom, age) +
sa propre représentation textuelle. Aucune persistance, aucune notification.
"""


class Personne:
    """Représente une personne avec un nom et un âge."""

    AGE_MIN = 0
    AGE_MAX = 100

    def __init__(self, nom: str, age: int):
        # Passage par les setters → validation centralisée (DRY)
        self.nom = nom
        self.age = age

    # ----- nom -----
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, valeur: str) -> None:
        if valeur is None or not isinstance(valeur, str) or not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        self.__nom = valeur.strip()

    # ----- age -----
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, valeur: int) -> None:
        if not isinstance(valeur, int) or isinstance(valeur, bool):
            raise ValueError("L'âge doit être un entier.")
        if valeur < self.AGE_MIN or valeur > self.AGE_MAX:
            raise ValueError(
                f"L'âge doit être compris entre {self.AGE_MIN} et {self.AGE_MAX} (reçu : {valeur})."
            )
        self.__age = valeur

    # ----- polymorphisme TP3 -----
    def afficher_details(self) -> str:
        """Méthode polymorphe — retourne la description textuelle.

        Redéfinie (override) dans Etudiant et Enseignant.
        Contrat LSP : retourne toujours une str non vide, ne lève jamais d'exception.
        """
        return f"{self.__nom}, {self.__age} ans"

    def __str__(self) -> str:
        return self.afficher_details()

    def __repr__(self) -> str:
        return f"Personne(nom={self.__nom!r}, age={self.__age})"
