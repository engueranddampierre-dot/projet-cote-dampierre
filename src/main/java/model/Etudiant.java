package main.model;
import java.util.ArrayList;

public class Etudiant extends Personne {
    private String numeroEtudiant;
    private double moyenne;
    public ArrayList<Cours> listeCours = new ArrayList<>();

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        setMoyenne(moyenne);
    }

    public String getNumeroEtudiant() { return numeroEtudiant; }
    public double getMoyenne() { return moyenne; }

    public void setMoyenne(double moyenne) {
        if (moyenne < 0 || moyenne > 20)
            throw new IllegalArgumentException("Moyenne invalide");
        this.moyenne = moyenne;
    }
    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Moyenne : " + moyenne;
    }
}