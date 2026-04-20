package model;


public class Enseignant extends Personne {
    private double salaire;

    public Enseignant(String nom, int age, double salaire) {
        super(nom, age);
        this.salaire = salaire;
    }

    public double getSalaire() { return salaire; }

    public String afficherDetails() {
        return super.afficherDetails() + " | Salaire : " + salaire;
    }
}