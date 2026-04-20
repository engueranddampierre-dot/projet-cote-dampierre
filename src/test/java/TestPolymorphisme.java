import model.Personne;
import model.Etudiant;
import model.Enseignant;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;

public class TestPolymorphisme {

    @Test
    void testAfficherDetailsEtudiant() {
        Etudiant e = new Etudiant("Alice", 20, "E001", 15.5);
        assertTrue(e.afficherDetails().contains("Alice"));
        assertTrue(e.afficherDetails().contains("15.5"));
    }

    @Test
    void testAfficherDetailsEnseignant() {
        Enseignant ens = new Enseignant("M. Dupont", 45, 3000.0);
        assertTrue(ens.afficherDetails().contains("M. Dupont"));
        assertTrue(ens.afficherDetails().contains("3000.0"));
    }

    @Test
    void testListeHeterogene() {
        ArrayList<Personne> liste = new ArrayList<>();
        liste.add(new Etudiant("Alice", 20, "E001", 15.5));
        liste.add(new Enseignant("M. Dupont", 45, 3000.0));
        assertEquals(2, liste.size());
    }
}