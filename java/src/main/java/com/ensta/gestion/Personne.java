package com.ensta.gestion;

/**
 * Classe mère du système de gestion étudiante.
 *
 * <ul>
 *   <li>TP1 : structure de base + héritage.</li>
 *   <li>TP2 : encapsulation — champs privés + setters validés.</li>
 *   <li>TP3 : afficherDetails() polymorphe (override dans Etudiant et Enseignant).</li>
 * </ul>
 *
 * SRP : représente uniquement l'identité d'une personne.
 * LSP : afficherDetails() retourne toujours une String non nulle, ne lève jamais d'exception.
 */
public class Personne {

    public static final int AGE_MIN = 0;
    public static final int AGE_MAX = 100;

    private String nom;
    private int age;

    public Personne(String nom, int age) {
        // Passage par les setters → validation centralisée
        setNom(nom);
        setAge(age);
    }

    // ----- nom -----
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        if (nom == null || nom.trim().isEmpty()) {
            throw new IllegalArgumentException("Le nom ne peut pas être vide.");
        }
        this.nom = nom.trim();
    }

    // ----- age -----
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age < AGE_MIN || age > AGE_MAX) {
            throw new IllegalArgumentException(
                "L'âge doit être compris entre " + AGE_MIN + " et " + AGE_MAX
                    + " (reçu : " + age + ")."
            );
        }
        this.age = age;
    }

    // ----- polymorphisme TP3 -----
    /**
     * Retourne la description textuelle de la personne.
     * Méthode redéfinie dans Etudiant et Enseignant.
     */
    public String afficherDetails() {
        return nom + ", " + age + " ans";
    }

    @Override
    public String toString() {
        return afficherDetails();
    }
}
