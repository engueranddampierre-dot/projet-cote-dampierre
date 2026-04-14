package main.model;

public class Personne {
    private String nom;
    private int age;

    public Personne(String nom, int age) {
        setNom(nom);
        setAge(age);
    }

    public String getNom() { return nom; }
    public int getAge() { return age; }

    public void setNom(String nom) {
        if (nom == null || nom.isEmpty())
            throw new IllegalArgumentException("Le nom ne peut pas être vide");
        this.nom = nom;
    }

    public void setAge(int age) {
        if (age < 0 || age > 100)
            throw new IllegalArgumentException("Age invalide");
        this.age = age;
    }
    public String afficherDetails() {
    return "Nom : " + nom + " | Age : " + age;
}
}