import model.*;
import manager.*;
import factory.*;
import strategy.*;
import adapter.*;
import decorator.*;

// Correction ici : on utilise strategy.MentionStrategy ou juste MentionStrategy
class MentionStandard implements MentionStrategy {
    public String calculer(double moyenne) {
        return (moyenne >= 10) ? "Admis" : "Ajourné";
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== TEST DU SYSTÈME DE GESTION ACADÉMIQUE ===\n");

        // 1. TEST SINGLETON
        ScolariteManager manager = ScolariteManager.getInstance();
        System.out.println("1. Singleton : Manager d'instance unique récupéré.");

        // 2. TEST FACTORY METHOD
        Etudiant etu = (Etudiant) PersonneFactory.createPersonne("ETUDIANT", "Jean Dupont", 21, "2026-ABC");
        Enseignant prof = (Enseignant) PersonneFactory.createPersonne("ENSEIGNANT", "Dr. Martin", 45, "3500.0");
        
        manager.ajouterEtudiant(etu);
        System.out.println("2. Factory : " + etu.getNom() + " et " + prof.getNom() + " créés.");

        // 3. TEST OBSERVER
        System.out.print("3. Observer : ");
        etu.setMoyenne(15.5); 

        // 4. TEST STRATEGY
        etu.setMentionStrategy(new MentionStandard());
        System.out.println("4. Strategy : Mention calculée -> " + etu.obtenirMention());

        // 5. TEST ADAPTER
        String legacyData = "Architecture_Logicielle;M. Lefebvre";
        Cours coursAdapte = LegacyCourseAdapter.transformer(legacyData);
        etu.listeCours.add(coursAdapte);
        System.out.println("5. Adapter : Cours '" + coursAdapte.nom + "' ajouté via format legacy.");

        // 6. TEST DECORATOR
        EtudiantBoursier etuBoursier = new EtudiantBoursier(etu);
        System.out.println("6. Decorator : " + etuBoursier.afficherStatutComplet());

        System.out.println("\n=== FIN DES TESTS ===");
    }
}