package adapter;
import model.Cours;

public class LegacyCourseAdapter {
    public static Cours transformer(String dataLegacy) {
        // Découpe "NomCours;NomProf" [cite: 18]
        String[] parts = dataLegacy.split(";");
        return new Cours(parts[0], parts[1]);
    }
}