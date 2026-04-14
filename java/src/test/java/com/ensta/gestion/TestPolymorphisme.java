package com.ensta.gestion;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests TP3 — Polymorphisme via afficherDetails().
 *
 * Vérifie qu'une List<Personne> hétérogène traite chaque élément
 * via la liaison dynamique, sans aucun instanceof dans la boucle (LSP + OCP).
 */
class TestPolymorphisme {

    @Test
    void personneAfficherDetails() {
        Personne p = new Personne("Alice", 30);
        String details = p.afficherDetails();
        assertTrue(details.contains("Alice"));
        assertTrue(details.contains("30"));
    }

    @Test
    void etudiantOverrideAfficherDetails() {
        Etudiant e = new Etudiant("Bob", 22, "E042", 15.5);
        String details = e.afficherDetails();
        assertTrue(details.contains("Bob"));
        assertTrue(details.contains("Étudiant") || details.contains("Etudiant"));
        assertTrue(details.contains("15"));
        assertTrue(details.contains("E042"));
    }

    @Test
    void enseignantOverrideAfficherDetails() {
        Enseignant ens = new Enseignant("Mme Curie", 45, "Physique", 3500.0);
        String details = ens.afficherDetails();
        assertTrue(details.contains("Curie"));
        assertTrue(details.contains("Enseignant"));
        assertTrue(details.contains("Physique"));
        assertTrue(details.contains("3500"));
    }

    @Test
    void listeHeterogenePolymorphe() {
        List<Personne> liste = new ArrayList<>();
        liste.add(new Etudiant("Alice", 20, "E001", 14.0));
        liste.add(new Enseignant("M. Dupont", 50, "Maths", 4000.0));
        liste.add(new Etudiant("Bob", 22, "E002", 16.5));
        liste.add(new Personne("Visiteur", 35));

        List<String> resultats = new ArrayList<>();
        // Aucun instanceof : c'est la JVM qui dispatche.
        for (Personne p : liste) {
            resultats.add(p.afficherDetails());
        }

        assertTrue(resultats.get(0).contains("Étudiant") || resultats.get(0).contains("Etudiant"));
        assertTrue(resultats.get(1).contains("Enseignant"));
        assertTrue(resultats.get(2).contains("Étudiant") || resultats.get(2).contains("Etudiant"));
        assertTrue(resultats.get(3).contains("Visiteur"));
    }

    @Test
    void lspSubstituabilite() {
        // Une fonction qui prend une Personne doit fonctionner pour toute sous-classe.
        assertNotNull(afficherAnonyme(new Personne("X", 20)));
        assertNotNull(afficherAnonyme(new Etudiant("Y", 21, "E1", 10.0)));
        assertNotNull(afficherAnonyme(new Enseignant("Z", 40, "Info", 3000.0)));
    }

    private String afficherAnonyme(Personne p) {
        return p.afficherDetails();
    }

    // ---------- Validation Enseignant ----------
    @Test
    void salaireNegatifRefuse() {
        assertThrows(IllegalArgumentException.class,
            () -> new Enseignant("X", 40, "Maths", -100.0));
    }

    @Test
    void matiereVideRefuse() {
        assertThrows(IllegalArgumentException.class,
            () -> new Enseignant("X", 40, "", 3000.0));
    }
}
