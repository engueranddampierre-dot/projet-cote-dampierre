package com.ensta.gestion;

/** Démonstration TP1 — Héritage. */
public class Main {

    public static void main(String[] args) {
        System.out.println("============================================================");
        System.out.println("TP1 — Héritage : Personne / Etudiant / Cours");
        System.out.println("============================================================");

        Cours maths = new Cours("Mathématiques", "M. Dupont");
        Cours physique = new Cours("Physique", "Mme Curie");
        Cours info = new Cours("Informatique", "M. Turing");

        Etudiant alice = new Etudiant("Alice Martin", 20, "E2024-001", 15.5);
        Etudiant bob = new Etudiant("Bob Durand", 22, "E2024-002", 13.0);

        alice.ajouterCours(maths);
        alice.ajouterCours(physique);
        alice.ajouterCours(info);

        bob.ajouterCours(maths);
        bob.ajouterCours(info);

        System.out.println();
        System.out.println(alice.afficherDetails());
        System.out.println();
        System.out.println(bob.afficherDetails());
    }
}
