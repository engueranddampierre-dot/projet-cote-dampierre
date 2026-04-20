package decorator;
import model.Etudiant;

public class EtudiantBoursier {
    private Etudiant etudiant;

    public EtudiantBoursier(Etudiant e) { this.etudiant = e; }

    public String afficherStatutComplet() {
        return etudiant.afficherDetails() + " | Statut : Boursier (Exonéré)";
    }
}