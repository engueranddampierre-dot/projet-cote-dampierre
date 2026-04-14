package com.ensta.gestion;

/**
 * Cours académique — SRP : représente uniquement un cours
 * (nom + professeur responsable). Aucune logique métier autre.
 */
public class Cours {

    private final String nomCours;
    private final String professeurResponsable;

    public Cours(String nomCours, String professeurResponsable) {
        if (nomCours == null || nomCours.trim().isEmpty()) {
            throw new IllegalArgumentException("Le nom du cours ne peut pas être vide.");
        }
        if (professeurResponsable == null || professeurResponsable.trim().isEmpty()) {
            throw new IllegalArgumentException("Le professeur responsable ne peut pas être vide.");
        }
        this.nomCours = nomCours.trim();
        this.professeurResponsable = professeurResponsable.trim();
    }

    public String getNomCours() {
        return nomCours;
    }

    public String getProfesseurResponsable() {
        return professeurResponsable;
    }

    @Override
    public String toString() {
        return nomCours + " (Prof : " + professeurResponsable + ")";
    }
}
