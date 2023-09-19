class Etudiant:
    "etudiant"
    
    def __init__(self, nom,prenom):
        self.__nom = nom
        self.__prenom = prenom
        self.__notes = []
        
    # Ajouter une note a l'etudiant
    def ajouter_note(self, note, coeff):
        self.__notes.append([note,coeff])
        
    # Ici on peut voir le nombre de notes
    def nbNotes(self):
        print(len(self.__notes))
        
    # Afficher les infos de l'etudiant
    def afficher(self):
        print("Nom : ", self.__nom)
        print("Prenom : ", self.__prenom)
        print("Notes : ", self.__notes)
    
    # Calculer la moyenne de l'etudiant
    def moyenne(self):
        somme = 0
        for note in self.__notes:
            somme += note[0] * note[1]
        return somme / len(self.__notes)

class Promotion:
    "promotion"
    def __init__(self, nom_promo):
        self.__nom_promo = nom_promo
        self.__etudiants = []
        
    # Ajouter un etudiant a la promo
    def ajouter_etudiant(self, etudiant):
        self.__etudiants.append(etudiant)
    
    # Nombre etudiants de la promo
    def nbre_etudiants(self):
        return len(self.__etudiants)
    

def main_etudiant():
    etudiant1 = Etudiant("akhal", "mohamad")
    etudiant1.ajouter_note(20,1)
    etudiant1.ajouter_note(0,1)
    etudiant1.afficher()
    etudiant1.nbNotes()
    print(etudiant1.moyenne())

def main_promo():
    