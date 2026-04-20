import model.Personne;
import model.Etudiant;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestEncapsulation {

    @Test
    void testAgeInvalideLeveException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Etudiant("Jean", -5, "ID123", 15.0);
        });
    }

    @Test
    void testNomVideLeveException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Etudiant("", 20, "ID789", 10.0);
        });
    }
}