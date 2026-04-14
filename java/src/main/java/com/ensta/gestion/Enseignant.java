package com.ensta.gestion;

/**
 * Enseignant : Personne + matière + salaire (TP3).
 * LSP : substituable à Personne, contrat afficherDetails() respecté.
 */
public class Enseignant extends Personne {

    public static final double SALAIRE_MIN = 0.0;

    private String matiere;
    private double salaire;

    public Enseignant(String nom, int age, String matiere, double salaire) {
        super(nom, age);
        setMatiere(matiere);
        setSalaire(salaire);
    }

    public String getMatiere() {
        return matiere;
    }

    public void setMatiere(String matiere) {
        if (matiere == null || matiere.trim().isEmpty()) {
            throw new IllegalArgumentException("La matière ne peut pas être vide.");
        }
        this.matiere = matiere.trim();
    }

    public double getSalaire() {
        return salaire;
    }

    public void setSalaire(double salaire) {
        if (salaire < SALAIRE_MIN) {
            throw new IllegalArgumentException(
                "Le salaire ne peut pas être négatif (reçu : " + salaire + ")."
            );
        }
        this.salaire = salaire;
    }

    @Override
    public String afficherDetails() {
        return "[Enseignant] " + super.afficherDetails()
            + " | Matière : " + matiere
            + " | Salaire : " + String.format("%.2f", salaire) + " €";
    }
}
