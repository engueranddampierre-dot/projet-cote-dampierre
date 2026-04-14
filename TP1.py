# ============================================================
# TP 1 - Héritage
# ============================================================

class Cours():
    def __init__(self, nom, prof):
        self.nom = nom
        self.prof = prof

    def __str__(self):
        return f"{self.nom} (resp. {self.prof})"


class Personne():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_details(self):
        return f"{self.nom}, {self.age} ans"


class Etudiant(Personne):
    def __init__(self, nom, age, numero, moyenne, liste_cours=None):
        super().__init__(nom, age)
        self.numero = numero
        self.moyenne = moyenne
        self.liste_cours = liste_cours if liste_cours is not None else []

    def ajouter_cours(self, cours):
        self.liste_cours.append(cours)

    def afficher_details(self):
        details = super().afficher_details()
        details += f"\n  Numéro : {self.numero}"
        details += f"\n  Moyenne : {self.moyenne}/20"
        details += f"\n  Cours : {', '.join(str(c) for c in self.liste_cours)}"
        return details


# ============================================================
# TP 2 - Encapsulation (Personne et Etudiant sécurisés)
# ============================================================

class Personne():
    def __init__(self, nom, age):
        if not nom or not nom.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self.__nom = nom
        self.age = age  # via setter

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 100:
            raise ValueError("L'âge doit être entre 0 et 100")
        self.__age = valeur

    def afficher_details(self):
        return f"{self.__nom}, {self.__age} ans"


class Etudiant(Personne):
    def __init__(self, nom, age, numero, moyenne, liste_cours=None):
        super().__init__(nom, age)
        self.__numero = numero
        self.moyenne = moyenne  # via setter
        self.__liste_cours = liste_cours if liste_cours is not None else []

    @property
    def numero(self):
        return self.__numero  # lecture seule

    @property
    def moyenne(self):
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, valeur):
        if valeur < 0 or valeur > 20:
            raise ValueError("La moyenne doit être entre 0 et 20")
        self.__moyenne = valeur

    def ajouter_cours(self, cours):
        self.__liste_cours.append(cours)

    def afficher_details(self):
        details = super().afficher_details()
        details += f"\n  Numéro : {self.__numero}"
        details += f"\n  Moyenne : {self.__moyenne}/20"
        details += f"\n  Cours : {', '.join(str(c) for c in self.__liste_cours)}"
        return details


# ============================================================
# TP 3 - Polymorphisme (ajout Enseignant)
# ============================================================

class Enseignant(Personne):
    def __init__(self, nom, age, matiere, salaire):
        super().__init__(nom, age)
        self.__matiere = matiere
        self.salaire = salaire  # via setter

    @property
    def matiere(self):
        return self.__matiere

    @property
    def salaire(self):
        return self.__salaire

    @salaire.setter
    def salaire(self, valeur):
        if valeur < 0:
            raise ValueError("Le salaire ne peut pas être négatif")
        self.__salaire = valeur

    def afficher_details(self):
        details = super().afficher_details()
        details += f"\n  Matière : {self.__matiere}"
        details += f"\n  Salaire : {self.__salaire} €"
        return details


# ============================================================
# MAIN - Démonstration des 3 TP
# ============================================================

if __name__ == "__main__":

    # --- TP1 : création et héritage ---
    cours_1 = Cours("Conception logicielle", "M. BA")
    cours_2 = Cours("Week-end de formation", "Les anciens")

    moi = Etudiant("Enguérand", 21, "20121991", 16.7, [cours_1, cours_2])
    print("=== TP1 - Héritage ===")
    print(moi.afficher_details())

    # --- TP2 : encapsulation et validation ---
    print("\n=== TP2 - Encapsulation ===")
    try:
        moi.moyenne = 25  # doit lever une erreur
    except ValueError as e:
        print(f"Erreur attendue : {e}")

    try:
        moi.age = -5  # doit lever une erreur
    except ValueError as e:
        print(f"Erreur attendue : {e}")

    # --- TP3 : polymorphisme ---
    print("\n=== TP3 - Polymorphisme ===")
    prof = Enseignant("M. BA", 45, "Conception logicielle", 3200)

    liste: list[Personne] = [moi, prof]

    for personne in liste:
        print(personne.afficher_details())  # liaison dynamique, pas de isinstance
        print()