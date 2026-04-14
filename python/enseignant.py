"""Module Enseignant — Hérite de Personne (TP3).

Démontre le polymorphisme : même méthode afficher_details(),
comportement spécifique selon le type réel de l'objet.

LSP : substituable à Personne. Contrat respecté (str retournée, pas d'exception).
"""

from personne import Personne


class Enseignant(Personne):
    """Un enseignant : une Personne avec une matière et un salaire."""

    SALAIRE_MIN = 0.0

    def __init__(self, nom: str, age: int, matiere: str, salaire: float):
        super().__init__(nom, age)
        if not matiere or not matiere.strip():
            raise ValueError("La matière ne peut pas être vide.")
        self.__matiere = matiere.strip()
        self.salaire = salaire  # passage par setter → validation

    # ----- matiere -----
    @property
    def matiere(self) -> str:
        return self.__matiere

    @matiere.setter
    def matiere(self, valeur: str) -> None:
        if not valeur or not valeur.strip():
            raise ValueError("La matière ne peut pas être vide.")
        self.__matiere = valeur.strip()

    # ----- salaire -----
    @property
    def salaire(self) -> float:
        return self.__salaire

    @salaire.setter
    def salaire(self, valeur: float) -> None:
        if not isinstance(valeur, (int, float)) or isinstance(valeur, bool):
            raise ValueError("Le salaire doit être un nombre.")
        if valeur < self.SALAIRE_MIN:
            raise ValueError(
                f"Le salaire ne peut pas être négatif (reçu : {valeur})."
            )
        self.__salaire = float(valeur)

    # ----- polymorphisme TP3 -----
    def afficher_details(self) -> str:
        base = super().afficher_details()
        return (
            f"[Enseignant] {base} | Matière : {self.__matiere} | "
            f"Salaire : {self.__salaire:.2f} €"
        )

    def __repr__(self) -> str:
        return (
            f"Enseignant(nom={self.nom!r}, age={self.age}, "
            f"matiere={self.__matiere!r}, salaire={self.__salaire})"
        )
