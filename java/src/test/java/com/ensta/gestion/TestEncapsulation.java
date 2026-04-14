package com.ensta.gestion;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests TP2 — Encapsulation et validation.
 */
class TestEncapsulation {

    @Nested
    class ValidationAge {
        @Test
        void ageNegatifRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Personne("Alice", -1));
        }

        @Test
        void ageTropGrandRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Personne("Alice", 101));
        }

        @Test
        void ageLimiteBasseAcceptee() {
            Personne p = new Personne("Bébé", 0);
            assertEquals(0, p.getAge());
        }

        @Test
        void ageLimiteHauteAcceptee() {
            Personne p = new Personne("Doyen", 100);
            assertEquals(100, p.getAge());
        }

        @Test
        void modifierAgeInvalideRefuseEtPreserveValeur() {
            Personne p = new Personne("Alice", 25);
            assertThrows(IllegalArgumentException.class, () -> p.setAge(150));
            assertEquals(25, p.getAge());
        }
    }

    @Nested
    class ValidationNom {
        @Test
        void nomVideRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Personne("", 25));
        }

        @Test
        void nomBlancsRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Personne("   ", 25));
        }

        @Test
        void nomNullRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Personne(null, 25));
        }
    }

    @Nested
    class ValidationMoyenne {
        @Test
        void moyenneNegativeRefuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Etudiant("Alice", 20, "E001", -0.1));
        }

        @Test
        void moyenneSuperieure20Refuse() {
            assertThrows(IllegalArgumentException.class,
                () -> new Etudiant("Alice", 20, "E001", 25.0));
        }

        @Test
        void modifierMoyenneInvalideRefuseEtPreserve() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 12.0);
            assertThrows(IllegalArgumentException.class, () -> e.setMoyenne(25.0));
            assertEquals(12.0, e.getMoyenne(), 0.001);
        }

        @Test
        void modifierMoyenneValideAcceptee() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 12.0);
            e.setMoyenne(15.5);
            assertEquals(15.5, e.getMoyenne(), 0.001);
        }

        @Test
        void moyenneLimiteBasse() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 0.0);
            assertEquals(0.0, e.getMoyenne(), 0.001);
        }

        @Test
        void moyenneLimiteHaute() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 20.0);
            assertEquals(20.0, e.getMoyenne(), 0.001);
        }
    }

    @Nested
    class EncapsulationStricte {
        @Test
        void numeroEtudiantLectureSeule() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 14.0);
            // Aucun setter exposé pour numeroEtudiant : la valeur est figée
            assertEquals("E001", e.getNumeroEtudiant());
            // Vérification réflexive : pas de méthode setNumeroEtudiant
            boolean setterTrouve = false;
            for (var m : Etudiant.class.getMethods()) {
                if (m.getName().equals("setNumeroEtudiant")) {
                    setterTrouve = true;
                    break;
                }
            }
            assertFalse(setterTrouve, "Aucun setter ne doit exposer numeroEtudiant.");
        }

        @Test
        void listeCoursCopieDefensive() {
            Etudiant e = new Etudiant("Alice", 20, "E001", 14.0);
            e.ajouterCours(new Cours("Maths", "M. Dupont"));
            List<Cours> liste = e.getListeCours();
            // La liste retournée est non modifiable : add() doit lever
            assertThrows(UnsupportedOperationException.class,
                () -> liste.add(new Cours("Hack", "Pirate")));
            // L'interne reste intact
            assertEquals(1, e.getListeCours().size());
        }
    }
}
