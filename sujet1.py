# 1. Fonctionnalités sur les notes :
def creer_etudiant(nom, prenom, notes):
    return [nom, prenom, notes]

def creer_promo(intitule, etudiants):
    return [intitule, etudiants]

def ajouter_note_etudiant(etudiant, note, coef):
    etudiant[2].append([note, coef])
    
def nombre_notes_etudiant(etudiant):
    return len(etudiant[2])

def moyenne_etudiant(etudiant):
    somme = 0
    for note in etudiant[2]:
        somme += note[0] * note[1]
    return somme / len(etudiant[2])

# fonction principale de test, creer l'etudiant et la promo et affiche les resultats des fonctions
def main():
    etudiant1 = creer_etudiant("Dupont", "Jean", [])
    ajouter_note_etudiant(etudiant1, 12, 1)
    print("Nombre de notes de l'étudiant : ", nombre_notes_etudiant(etudiant1))
    ajouter_note_etudiant(etudiant1, 14, 1)
    print("Nombre de notes de l'étudiant : ", nombre_notes_etudiant(etudiant1))
    print("Moyenne de l'étudiant : ", moyenne_etudiant(etudiant1))
    etudiant2 = creer_etudiant("Durand", "Pierre", [])
    creer_promo("L3", [etudiant1, etudiant2])
    
main()