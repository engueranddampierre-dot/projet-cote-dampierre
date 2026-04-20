"""Module PersonneFactory — Pattern FACTORY METHOD.

Encapsule la logique de création des objets Personne (Etudiant, Enseignant).
Le code client n'a pas besoin de connaître les constructeurs concrets :
il passe un type et des paramètres, la factory se charge du reste.

OCP : pour ajouter un nouveau type (ex: Doctorant), on ajoute une branche
      sans modifier le code client existant.
DIP : le client dépend de l'abstraction Personne, pas des classes concrètes.
"""

from enseignant import Enseignant
from etudiant import Etudiant
from personne import Personne


class PersonneFactory:
    """Factory de création de Personne (Etudiant ou Enseignant).

    Usage :
        etudiant = PersonneFactory.creer("etudiant",
            nom="Alice", age=20, numero_etudiant="E001", moyenne=15.0)
        prof = PersonneFactory.creer("enseignant",
            nom="Dr. Martin", age=45, matiere="Maths", salaire=3500.0)
    """

    @staticmethod
    def creer(type_personne: str, **kwargs) -> Personne:
        """Crée et retourne une instance de Personne selon le type demandé.

        Args:
            type_personne: "etudiant" ou "enseignant" (insensible à la casse).
            **kwargs: paramètres transmis au constructeur concret.

        Returns:
            Instance d'Etudiant ou d'Enseignant.

        Raises:
            ValueError: si le type est inconnu.
        """
        type_lower = type_personne.strip().lower()

        if type_lower == "etudiant":
            return Etudiant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                numero_etudiant=kwargs["numero_etudiant"],
                moyenne=kwargs.get("moyenne", 0.0),
            )
        elif type_lower in ("enseignant", "professeur"):
            return Enseignant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                matiere=kwargs["matiere"],
                salaire=kwargs["salaire"],
            )
        else:
            raise ValueError(
                f"Type de personne inconnu : '{type_personne}'. "
                f"Types valides : 'etudiant', 'enseignant'."
            )
