package main;
import main.model.Etudiant;
import main.model.Cours;

public class Main {
    public static void main(String[] args) {
        Cours c1 = new Cours("Maths", "M. Dupont");
        Cours c2 = new Cours("Physique", "Mme Martin");

        Etudiant e1 = new Etudiant("Alice", 20, "E001", 15.5);

        e1.listeCours.add(c1);
        e1.listeCours.add(c2);

        System.out.println("Nom : " + e1.getNom());
        System.out.println("Age : " + e1.getAge());
        System.out.println("Numéro : " + e1.getNumeroEtudiant());
        System.out.println("Moyenne : " + e1.getMoyenne());
        System.out.println("Cours : ");
        for (Cours c : e1.listeCours) {
            System.out.println("  - " + c.nom + " / " + c.professeur);
        }
    }
}