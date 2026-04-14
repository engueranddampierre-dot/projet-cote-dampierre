import main.model.Personne;
import main.model.Etudiant;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestEncapsulation {

    @Test
    void testAgeInvalideLeveException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Personne("Alice", -5);
        });
    }

    @Test
    void testMoyenneInvalideLeveException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Etudiant("Alice", 20, "E001", 25.0);
        });
    }

    @Test
    void testNomVideLeveException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Personne("", 20);
        });
    }
}