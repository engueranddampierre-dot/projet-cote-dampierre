# Diagramme UML — Gestion Étudiante

## Diagramme de classes (PlantUML)

À coller dans [PlantUML Online](https://www.plantuml.com/plantuml/uml/) ou à compiler avec `plantuml uml.puml`.

```plantuml
@startuml GestionEtudiante

skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam linetype ortho
hide empty methods
hide empty fields

class Cours {
  - nom_cours : String
  - professeur_responsable : String
  + getNomCours() : String
  + getProfesseurResponsable() : String
  + toString() : String
}

class Personne {
  + {static} AGE_MIN : int = 0
  + {static} AGE_MAX : int = 100
  - nom : String
  - age : int
  + Personne(nom, age)
  + getNom() : String
  + setNom(nom) : void
  + getAge() : int
  + setAge(age) : void
  + afficherDetails() : String
  + toString() : String
}

class Etudiant {
  + {static} MOYENNE_MIN : double = 0.0
  + {static} MOYENNE_MAX : double = 20.0
  - numeroEtudiant : String  <<final>>
  - moyenne : double
  - listeCours : List<Cours>
  + Etudiant(nom, age, numero, moyenne)
  + getNumeroEtudiant() : String
  + getMoyenne() : double
  + setMoyenne(m) : void
  + getListeCours() : List<Cours>
  + ajouterCours(c : Cours) : void
  + afficherDetails() : String  <<override>>
}

class Enseignant {
  + {static} SALAIRE_MIN : double = 0.0
  - matiere : String
  - salaire : double
  + Enseignant(nom, age, matiere, salaire)
  + getMatiere() : String
  + setMatiere(m) : void
  + getSalaire() : double
  + setSalaire(s) : void
  + afficherDetails() : String  <<override>>
}

Personne <|-- Etudiant
Personne <|-- Enseignant
Etudiant "1" *-- "0..*" Cours : possède >

note right of Personne
  Classe mère — identité.
  afficherDetails() est
  redéfinie dans chaque
  sous-classe (polymorphisme).
end note

note right of Etudiant
  TP2 : moyenne validée [0,20]
  numéro en lecture seule
  liste_cours : copie défensive
end note

@enduml
```

## Relations

- **Héritage** : `Etudiant` et `Enseignant` héritent de `Personne` (relation *est-un*).
- **Composition** : `Etudiant` possède 0..N `Cours` (relation *a-un*).
- **Polymorphisme** : `afficherDetails()` définie dans `Personne`, redéfinie dans `Etudiant` et `Enseignant`.

## Respect SOLID

| Principe | Application |
| --- | --- |
| **S** | Chaque classe = 1 responsabilité (identité, cours, rôle pédagogique). |
| **O** | Ajouter un `Doctorant extends Etudiant` → aucune modification du code existant. |
| **L** | `Etudiant`/`Enseignant` substituables à `Personne` sans casser le contrat. |
| **I** | Pas d'interface fourre-tout ; on pourrait introduire `IAffichable` sans impact. |
| **D** | Les dépendances concrètes (persistance, notifications) sont absentes du domaine — prêt pour injection. |
