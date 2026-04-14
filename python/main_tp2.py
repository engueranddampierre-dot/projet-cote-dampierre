"""Programme de démonstration TP2 — Encapsulation et validation.

Tente de violer les invariants pour montrer que les setters refusent.
"""

from etudiant import Etudiant


def tenter(description: str, action) -> None:
    print(f"\n>>> {description}")
    try:
        action()
        print("    → OK")
    except (ValueError, TypeError) as exc:
        print(f"    → REFUSÉ : {exc}")


def main() -> None:
    print("=" * 60)
    print("TP2 — Encapsulation et validation")
    print("=" * 60)

    alice = Etudiant("Alice", 20, "E2024-001", 14.0)
    print(f"\nÉtudiante créée : {alice.afficher_details()}")

    tenter("Modifier la moyenne à 18.5 (valide)", lambda: setattr(alice, "moyenne", 18.5))
    print(f"    Moyenne actuelle : {alice.moyenne}")

    tenter("Modifier la moyenne à 25 (invalide, > 20)", lambda: setattr(alice, "moyenne", 25.0))
    print(f"    Moyenne préservée : {alice.moyenne}")

    tenter("Modifier la moyenne à -3 (invalide, < 0)", lambda: setattr(alice, "moyenne", -3.0))
    print(f"    Moyenne préservée : {alice.moyenne}")

    tenter("Modifier l'âge à 150 (invalide)", lambda: setattr(alice, "age", 150))
    print(f"    Âge préservé : {alice.age}")

    tenter("Créer une Personne avec nom vide", lambda: Etudiant("", 20, "E999"))


if __name__ == "__main__":
    main()
