"""Programme de démonstration TP1 — Héritage.

Crée des étudiants, ajoute des cours, affiche les détails.
"""

from cours import Cours
from etudiant import Etudiant


def main() -> None:
    print("=" * 60)
    print("TP1 — Héritage : Personne / Etudiant / Cours")
    print("=" * 60)

    # Création des cours
    maths = Cours("Mathématiques", "M. Dupont")
    physique = Cours("Physique", "Mme Curie")
    info = Cours("Informatique", "M. Turing")

    # Création des étudiants
    alice = Etudiant("Alice Martin", 20, "E2024-001", 15.5)
    bob = Etudiant("Bob Durand", 22, "E2024-002", 13.0)

    # Inscription aux cours
    alice.ajouter_cours(maths)
    alice.ajouter_cours(physique)
    alice.ajouter_cours(info)

    bob.ajouter_cours(maths)
    bob.ajouter_cours(info)

    # Affichage
    for etu in (alice, bob):
        print()
        print(etu.afficher_details())


if __name__ == "__main__":
    main()
