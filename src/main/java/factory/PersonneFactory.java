package factory;
import model.*;

public class PersonneFactory {
    public static Personne createPersonne(String type, String nom, int age, String info) {
        if (type.equalsIgnoreCase("ETUDIANT")) {
            return new Etudiant(nom, age, info, 0.0); // info = numéro étudiant [cite: 10, 15]
        } else if (type.equalsIgnoreCase("ENSEIGNANT")) {
            return new Enseignant(nom, age, Double.parseDouble(info)); // info = salaire
        }
        return null;
    }
}