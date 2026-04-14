package com.ensta.gestion;

import java.util.ArrayList;
import java.util.List;

/** Démonstration TP3 — Polymorphisme : liste hétérogène de Personne. */
public class MainTp3 {

    public static void main(String[] args) {
        System.out.println("============================================================");
        System.out.println("TP3 — Polymorphisme : liste hétérogène de Personne");
        System.out.println("============================================================");

        Cours maths = new Cours("Mathématiques", "M. Dupont");
        Cours physique = new Cours("Physique", "Mme Curie");

        Etudiant alice = new Etudiant("Alice Martin", 20, "E2024-001", 15.5);
        alice.ajouterCours(maths);
        alice.ajouterCours(physique);

        Etudiant bob = new Etudiant("Bob Durand", 22, "E2024-002", 12.0);
        bob.ajouterCours(maths);

        Enseignant dupont = new Enseignant("M. Dupont", 50, "Mathématiques", 4200.0);
        Enseignant curie = new Enseignant("Mme Curie", 45, "Physique", 4500.0);

        List<Personne> membres = new ArrayList<>();
        membres.add(alice);
        membres.add(dupont);
        membres.add(bob);
        membres.add(curie);

        System.out.println();
        for (Personne membre : membres) {
            // Aucun instanceof — la JVM dispatche au bon afficherDetails().
            System.out.println(membre.afficherDetails());
        }
    }
}
