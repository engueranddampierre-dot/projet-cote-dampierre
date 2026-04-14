package com.ensta.gestion;

/** Démonstration TP2 — Encapsulation et validation. */
public class MainTp2 {

    public static void main(String[] args) {
        System.out.println("============================================================");
        System.out.println("TP2 — Encapsulation et validation");
        System.out.println("============================================================");

        Etudiant alice = new Etudiant("Alice", 20, "E2024-001", 14.0);
        System.out.println("\nÉtudiante créée : " + alice.afficherDetails());

        tenter("Modifier la moyenne à 18.5 (valide)", () -> alice.setMoyenne(18.5));
        System.out.println("    Moyenne actuelle : " + alice.getMoyenne());

        tenter("Modifier la moyenne à 25 (invalide)", () -> alice.setMoyenne(25.0));
        System.out.println("    Moyenne préservée : " + alice.getMoyenne());

        tenter("Modifier la moyenne à -3 (invalide)", () -> alice.setMoyenne(-3.0));
        System.out.println("    Moyenne préservée : " + alice.getMoyenne());

        tenter("Modifier l'âge à 150 (invalide)", () -> alice.setAge(150));
        System.out.println("    Âge préservé : " + alice.getAge());

        tenter("Créer un Etudiant avec nom vide", () -> new Etudiant("", 20, "E999", 10.0));
    }

    private static void tenter(String description, Runnable action) {
        System.out.println("\n>>> " + description);
        try {
            action.run();
            System.out.println("    → OK");
        } catch (RuntimeException ex) {
            System.out.println("    → REFUSÉ : " + ex.getMessage());
        }
    }
}
