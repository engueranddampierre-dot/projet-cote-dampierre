from cours import Cours
from etudiant import Etudiant
from etudiant_decorator import EtudiantBoursier, EtudiantDelegue
from legacy_adapter import LegacyCoursAdapter, LegacyCoursSystem
from personne_factory import PersonneFactory
from scolarite_manager import ScolariteManager
from strategy_tri import (
    ContexteTri,
    MentionStrategy,
    TriParMoyenne,
    TriParNom,
)


def separateur(titre: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {titre}")
    print(f"{'='*60}")


def main() -> None:

    # ==================================================================
    # 1. SINGLETON — ScolariteManager
    # ==================================================================
    separateur("1. SINGLETON — ScolariteManager")

    manager1 = ScolariteManager.get_instance()
    manager2 = ScolariteManager.get_instance()
    print(f"manager1 is manager2 ? {manager1 is manager2}")  # True
    print(f"id(manager1) = {id(manager1)}")
    print(f"id(manager2) = {id(manager2)}")

    # ==================================================================
    # 2. FACTORY METHOD — PersonneFactory
    # ==================================================================
    separateur("2. FACTORY METHOD — PersonneFactory")

    alice = PersonneFactory.creer(
        "etudiant", nom="Alice Dupont", age=20,
        numero_etudiant="E001", moyenne=15.5,
    )
    bob = PersonneFactory.creer(
        "etudiant", nom="Bob Martin", age=22,
        numero_etudiant="E002", moyenne=12.0,
    )
    charlie = PersonneFactory.creer(
        "etudiant", nom="Charlie Petit", age=21,
        numero_etudiant="E003", moyenne=17.0,
    )
    prof = PersonneFactory.creer(
        "enseignant", nom="Dr. Curie", age=45,
        matiere="Physique", salaire=3500.0,
    )

    print(alice)
    print(bob)
    print(charlie)
    print(prof)

    # ==================================================================
    # 4. ADAPTER — Données Legacy → objets Cours
    # ==================================================================
    separateur("4. ADAPTER — Legacy → Cours")

    legacy = LegacyCoursSystem()
    legacy.ajouter_donnee("Mathématiques|Dr. Martin")
    legacy.ajouter_donnee("Physique|Dr. Curie")
    legacy.ajouter_donnee("Informatique|Dr. Turing")
    legacy.ajouter_donnee("DonnéeInvalide")  # sera ignorée

    adapter = LegacyCoursAdapter(legacy)
    cours_adaptes = adapter.get_cours()

    print("Cours convertis depuis le système legacy :")
    for c in cours_adaptes:
        print(f"  → {c}")

    # Ajout de cours aux étudiants
    for etudiant in (alice, bob, charlie):
        for c in cours_adaptes:
            etudiant.ajouter_cours(c)

    # ==================================================================
    # 6. OBSERVER — Enregistrement + notifications automatiques
    # ==================================================================
    separateur("6. OBSERVER — Enregistrement auprès du manager")

    manager = ScolariteManager.get_instance()
    # ajouter_etudiant() enregistre automatiquement le manager comme observer
    manager.ajouter_etudiant(alice)
    manager.ajouter_etudiant(bob)
    manager.ajouter_etudiant(charlie)

    print(f"\n{manager.afficher_statistiques()}")

    print("\n--- Modification de la moyenne de Bob (12 → 16) ---")
    bob.moyenne = 16.0  # déclenche mise_a_jour() sur le manager
    print(f"\n{manager.afficher_statistiques()}")

    # ==================================================================
    # 3. DECORATOR — EtudiantBoursier, EtudiantDelegue
    # ==================================================================
    separateur("3. DECORATOR — Ajout de responsabilités")

    alice_boursiere = EtudiantBoursier(alice, montant_bourse=5000.0)
    print(alice_boursiere)

    # On peut empiler les décorateurs !
    alice_boursiere_deleguee = EtudiantDelegue(
        alice_boursiere, promotion="L3 Informatique"
    )
    print(alice_boursiere_deleguee)

    charlie_delegue = EtudiantDelegue(charlie, promotion="M1 Maths")
    print(charlie_delegue)

    # Le décorateur est transparent : isinstance fonctionne
    print(f"\nisinstance(alice_boursiere, Etudiant) ? "
          f"{isinstance(alice_boursiere, Etudiant)}")

    # ==================================================================
    # 5. STRATEGY — Tri dynamique
    # ==================================================================
    separateur("5. STRATEGY — Tri dynamique des étudiants")

    etudiants = [alice, bob, charlie]
    ctx = ContexteTri(TriParMoyenne())

    print("\n--- Tri par moyenne (décroissant) ---")
    for e in ctx.executer(etudiants):
        print(f"  {e.nom:20s} → {e.moyenne:.2f}/20")

    ctx.set_strategy(TriParNom())
    print("\n--- Tri par nom (alphabétique) ---")
    for e in ctx.executer(etudiants):
        print(f"  {e.nom:20s} → {e.moyenne:.2f}/20")

    ctx.set_strategy(MentionStrategy())
    print("\n--- Tri par mention ---")
    mention_strat = MentionStrategy()
    for e in ctx.executer(etudiants):
        mention = mention_strat.calculer_mention(e.moyenne)
        print(f"  {e.nom:20s} → {e.moyenne:.2f}/20  ({mention})")

    # ==================================================================
    # Récapitulatif final
    # ==================================================================
    separateur("RÉCAPITULATIF FINAL")
    print(manager.afficher_statistiques())
    print("\nListe complète :")
    for e in manager.etudiants:
        print(f"  {e}")


if __name__ == "__main__":
    main()
