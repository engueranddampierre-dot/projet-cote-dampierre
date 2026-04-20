package model;
import java.util.ArrayList;
import strategy.MentionStrategy;
import manager.ScolariteManager;
public class Etudiant extends Personne {
    private String numeroEtudiant;
    private double moyenne;
    public ArrayList<Cours> listeCours = new ArrayList<>();
    private MentionStrategy mentionStrategy; // Pattern Strategy

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        setMoyenne(moyenne);
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
        // On utilise le chemin direct car on a importé la classe ou on utilise le nouveau package
        manager.ScolariteManager.getInstance().notifierChangementNote(this);
}

    public void setMentionStrategy(MentionStrategy strategy) {
        this.mentionStrategy = strategy;
    }

    public String obtenirMention() {
        return (mentionStrategy != null) ? mentionStrategy.calculer(this.moyenne) : "Pas de stratégie";
    }

    @Override
    public String afficherDetails() {
        return super.afficherDetails() + " | Etudiant n°" + numeroEtudiant + " | Moyenne : " + moyenne;
    }
    
    public double getMoyenne() { return moyenne; }
}

