package com.ensta.gestion;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Étudiant : Personne + numéro étudiant + moyenne + cours.
 *
 * Encapsulation TP2 : moyenne validée [0,20], numéro en lecture seule,
 * liste de cours protégée (copie défensive).
 *
 * Polymorphisme TP3 : afficherDetails() override.
 */
public class Etudiant extends Personne {

    public static final double MOYENNE_MIN = 0.0;
    public static final double MOYENNE_MAX = 20.0;

    private final String numeroEtudiant;   // lecture seule après création
    private double moyenne;
    private final List<Cours> listeCours;

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age);
        if (numeroEtudiant == null || numeroEtudiant.trim().isEmpty()) {
            throw new IllegalArgumentException("Le numéro d'étudiant ne peut pas être vide.");
        }
        this.numeroEtudiant = numeroEtudiant.trim();
        this.listeCours = new ArrayList<>();
        setMoyenne(moyenne);
    }

    public Etudiant(String nom, int age, String numeroEtudiant) {
        this(nom, age, numeroEtudiant, 0.0);
    }

    // ----- numero etudiant : lecture seule -----
    public String getNumeroEtudiant() {
        return numeroEtudiant;
    }

    // ----- moyenne -----
    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        if (moyenne < MOYENNE_MIN || moyenne > MOYENNE_MAX) {
            throw new IllegalArgumentException(
                "La moyenne doit être comprise entre " + MOYENNE_MIN + " et "
                    + MOYENNE_MAX + " (reçu : " + moyenne + ")."
            );
        }
        this.moyenne = moyenne;
    }

    // ----- liste cours : accès contrôlé -----
    public List<Cours> getListeCours() {
        // Copie défensive : modifier la liste retournée n'altère pas l'interne.
        return Collections.unmodifiableList(new ArrayList<>(listeCours));
    }

    public void ajouterCours(Cours cours) {
        if (cours == null) {
            throw new IllegalArgumentException("Le cours ne peut pas être null.");
        }
        listeCours.add(cours);
    }

    // ----- polymorphisme TP3 -----
    @Override
    public String afficherDetails() {
        StringBuilder sb = new StringBuilder("[Étudiant] ")
            .append(super.afficherDetails())
            .append(" | N° ").append(numeroEtudiant)
            .append(" | Moyenne : ").append(String.format("%.2f", moyenne)).append("/20")
            .append(" | Cours : ");
        if (listeCours.isEmpty()) {
            sb.append("aucun cours");
        } else {
            for (int i = 0; i < listeCours.size(); i++) {
                if (i > 0) sb.append(", ");
                sb.append(listeCours.get(i).getNomCours());
            }
        }
        return sb.toString();
    }
}
