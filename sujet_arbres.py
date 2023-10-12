class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)
    
    def somme(self):
        somme = self.valeur
        for enfant in self.enfants:
            somme += enfant.somme()
        return somme

racine = Noeud(0)
gauche = Noeud(1)
droite = Noeud(2)
gouche_gauche = Noeud(3)
gauche_droite = Noeud(4)
droite_gauche = Noeud(5)
gauche_droite = Noeud(6)

racine.ajouter_enfant(gauche)
racine.ajouter_enfant(droite)
gauche.ajouter_enfant(gouche_gauche)
gauche.ajouter_enfant(gauche_droite)
droite.ajouter_enfant(droite_gauche)
droite.ajouter_enfant(gauche_droite)

racine.afficher()

print(racine.somme())
