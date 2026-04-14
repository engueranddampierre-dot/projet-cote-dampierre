"""Programme de démonstration TP3 — Polymorphisme.

Une liste de Personne contient des Etudiant ET des Enseignant.
La boucle appelle afficher_details() — la liaison dynamique
sélectionne automatiquement la bonne implémentation.

Aucun isinstance / type() dans la boucle = polymorphisme pur.
"""

from typing import List

from cours import Cours
from enseignant import Enseignant
from etudiant import Etudiant
from personne import Personne


def main() -> None:
    print("=" * 60)
    print("TP3 — Polymorphisme : liste hétérogène de Personne")
    print("=" * 60)

    # Cours
    maths = Cours("Mathématiques", "M. Dupont")
    physique = Cours("Physique", "Mme Curie")

    # Étudiants
    alice = Etudiant("Alice Martin", 20, "E2024-001", 15.5)
    alice.ajouter_cours(maths)
    alice.ajouter_cours(physique)

    bob = Etudiant("Bob Durand", 22, "E2024-002", 12.0)
    bob.ajouter_cours(maths)

    # Enseignants
    dupont = Enseignant("M. Dupont", 50, "Mathématiques", 4200.0)
    curie = Enseignant("Mme Curie", 45, "Physique", 4500.0)

    # Liste hétérogène typée Personne
    membres: List[Personne] = [alice, dupont, bob, curie]

    print()
    for membre in membres:
        # Polymorphisme : aucun isinstance — la JVM/Python dispatche tout seul.
        print(membre.afficher_details())


if __name__ == "__main__":
    main()
