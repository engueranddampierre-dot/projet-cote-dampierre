package com.ensta.gestion;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests TP1 — Héritage Personne / Etudiant / Cours.
 * Cycle TDD : ces tests sont écrits AVANT l'implémentation (RED → GREEN → REFACTOR).
 */
class TestHeritage {

    @Nested
    class CoursTests {
        @Test
        void creationCoursValide() {
            Cours c = new Cours("Mathématiques", "M. Dupont");
            assertEquals("Mathématiques", c.getNomCours());
            assertEquals("M. Dupont", c.getProfesseurResponsable());
        }

        @Test
        void toStringContientNomEtProf() {
            Cours c = new Cours("Physique", "Mme Curie");
            String s = c.toString();
            assertTrue(s.contains("Physique"));
            assertTrue(s.contains("Curie"));
        }

        @Test
        void coursNomVideRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Cours("", "M. Dupont"));
        }

        @Test
        void coursProfVideRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Cours("Maths", "   "));
        }
    }

    @Nested
    class PersonneTests {
        @Test
        void creationPersonneValide() {
            Personne p = new Personne("Alice", 25);
            assertEquals("Alice", p.getNom());
            assertEquals(25, p.getAge());
        }

        @Test
        void toStringPersonne() {
            Personne p = new Personne("Bob", 30);
            String s = p.toString();
            assertTrue(s.contains("Bob"));
            assertTrue(s.contains("30"));
        }
    }

    @Nested
    class EtudiantHeritageTests {
        @Test
        void etudiantEstUnePersonne() {
            Etudiant e = new Etudiant("Charlie", 20, "E001", 14.5);
            assertInstanceOf(Personne.class, e);
            assertInstanceOf(Etudiant.class, e);
        }

        @Test
        void etudiantHeriteAttributsPersonne() {
            Etudiant e = new Etudiant("Charlie", 20, "E001", 14.5);
            assertEquals("Charlie", e.getNom());
            assertEquals(20, e.getAge());
        }

        @Test
        void etudiantAttributsSpecifiques() {
            Etudiant e = new Etudiant("Charlie", 20, "E001", 14.5);
            assertEquals("E001", e.getNumeroEtudiant());
            assertEquals(14.5, e.getMoyenne(), 0.001);
            assertTrue(e.getListeCours().isEmpty());
        }

        @Test
        void ajouterCours() {
            Etudiant e = new Etudiant("Charlie", 20, "E001");
            e.ajouterCours(new Cours("Maths", "M. Dupont"));
            e.ajouterCours(new Cours("Physique", "Mme Curie"));
            assertEquals(2, e.getListeCours().size());
            assertEquals("Maths", e.getListeCours().get(0).getNomCours());
        }

        @Test
        void ajouterCoursNullRefuse() {
            Etudiant e = new Etudiant("Charlie", 20, "E001");
            assertThrows(IllegalArgumentException.class, () -> e.ajouterCours(null));
        }

        @Test
        void afficherDetailsEtudiantComplet() {
            Etudiant e = new Etudiant("Charlie", 20, "E001", 14.5);
            e.ajouterCours(new Cours("Maths", "M. Dupont"));
            String s = e.afficherDetails();
            assertTrue(s.contains("Charlie"));
            assertTrue(s.contains("E001"));
            assertTrue(s.contains("14"));
            assertTrue(s.contains("Maths"));
        }
    }
}
