package manager;
import model.Etudiant;
import java.util.ArrayList;
import java.util.List;

public class ScolariteManager {
    private static ScolariteManager instance;
    private List<Etudiant> etudiants = new ArrayList<>();

    private ScolariteManager() {} // Constructeur privé (Singleton) [cite: 14]

    public static ScolariteManager getInstance() {
        if (instance == null) instance = new ScolariteManager();
        return instance;
    }

    public void ajouterEtudiant(Etudiant e) {
        etudiants.add(e);
    }

    // Méthode appelée par l'Etudiant quand sa moyenne change (Observer) 
    public void notifierChangementNote(Etudiant e) {
        System.out.println("[OBSERVER] ScolariteManager informé : " + e.getNom() + " a une nouvelle moyenne de " + e.getMoyenne());
    }
}
