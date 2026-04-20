from typing import List, Optional

from cours import Cours


# ---------------------------------------------------------------------------
# Système Legacy simulé
# ---------------------------------------------------------------------------
class LegacyCoursSystem:
    """Ancien système fournissant les cours au format « NomCours|Professeur ».

    Simule une source de données externe qu'on ne peut pas modifier.
    """

    def __init__(self) -> None:
        self.__data: List[str] = []

    def ajouter_donnee(self, donnee: str) -> None:
        """Ajoute une donnée legacy brute."""
        self.__data.append(donnee)

    def get_cours_legacy(self) -> List[str]:
        """Retourne les cours au format legacy (liste de strings)."""
        return list(self.__data)


# ---------------------------------------------------------------------------
# Adaptateur : Legacy → Cours
# ---------------------------------------------------------------------------
class LegacyCoursAdapter:
    """Adapte les données du LegacyCoursSystem en objets Cours.

    Usage :
        legacy = LegacyCoursSystem()
        legacy.ajouter_donnee("Mathématiques|Dr. Martin")
        legacy.ajouter_donnee("Physique|Dr. Curie")

        adapter = LegacyCoursAdapter(legacy)
        cours_list = adapter.get_cours()   # → [Cours(...), Cours(...)]
    """

    SEPARATEUR = "|"

    def __init__(self, legacy_system: LegacyCoursSystem):
        self.__legacy = legacy_system

    def get_cours(self) -> List[Cours]:
        """Convertit toutes les données legacy en objets Cours."""
        cours_list: List[Cours] = []
        for raw in self.__legacy.get_cours_legacy():
            cours = self._convertir(raw)
            if cours is not None:
                cours_list.append(cours)
        return cours_list

    def _convertir(self, donnee_legacy: str) -> Optional[Cours]:
        """Convertit une chaîne legacy en objet Cours.

        Format attendu : "NomCours|Professeur"
        Retourne None si le format est invalide (robustesse).
        """
        parts = donnee_legacy.split(self.SEPARATEUR)
        if len(parts) != 2:
            print(
                f"  [Adapter] Format invalide ignoré : '{donnee_legacy}' "
                f"(attendu : 'NomCours{self.SEPARATEUR}Professeur')"
            )
            return None
        nom_cours, professeur = parts[0].strip(), parts[1].strip()
        if not nom_cours or not professeur:
            print(f"  [Adapter] Donnée incomplète ignorée : '{donnee_legacy}'")
            return None
        return Cours(nom_cours, professeur)
