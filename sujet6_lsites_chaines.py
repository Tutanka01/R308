class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class ListeChainee:
    def __init__(self):
        self.tete = None

    def ajouter_fin(self, valeur):
        nouveau_noeud = Noeud(valeur)
        if self.tete is None:
            self.tete = nouveau_noeud
            return
        noeud_courant = self.tete
        while noeud_courant.suivant is not None:
            noeud_courant = noeud_courant.suivant
        noeud_courant.suivant = nouveau_noeud

    def ajouter_debut(self, valeur):
        nouveau_noeud = Noeud(valeur)
        nouveau_noeud.suivant = self.tete
        self.tete = nouveau_noeud

    def supprimer(self, valeur):
        if self.tete is None:
            return
        if self.tete.valeur == valeur:
            self.tete = self.tete.suivant
            return
        noeud_courant = self.tete
        while noeud_courant.suivant is not None:
            if noeud_courant.suivant.valeur == valeur:
                noeud_courant.suivant = noeud_courant.suivant.suivant
                return
            noeud_courant = noeud_courant.suivant

    def afficher(self):
        noeud_courant = self.tete
        while noeud_courant is not None:
            print(noeud_courant.valeur)
            noeud_courant = noeud_courant.suivant

    def print_recursif(self):
        noeud_courant = self.tete
        while noeud_courant is not None:
            print(noeud_courant.valeur)
            noeud_courant = noeud_courant.suivant

    def print_rev_recursif(self, noeud=None):
        if noeud is None:
            noeud = self.tete
        if noeud is not None:
            self.print_rev_recursif(noeud.suivant)
            print(noeud.valeur)

    def insert(self, valeur, index):
        nouveau_noeud = Noeud(valeur)
        if index == 0:
            nouveau_noeud.suivant = self.tete
            self.tete = nouveau_noeud
            return
        noeud_courant = self.tete
        for i in range(index - 1):
            if noeud_courant is None:
                return
            noeud_courant = noeud_courant.suivant
        nouveau_noeud.suivant = noeud_courant.suivant
        noeud_courant.suivant = nouveau_noeud

    def reverse(self):
        noeud_precedent = None
        noeud_courant = self.tete
        while noeud_courant is not None:
            noeud_suivant = noeud_courant.suivant
            noeud_courant.suivant = noeud_precedent
            noeud_precedent = noeud_courant
            noeud_courant = noeud_suivant
        self.tete = noeud_precedent

    def nb(self):
        count = 0
        noeud_courant = self.tete
        while noeud_courant is not None:
            count += 1
            noeud_courant = noeud_courant.suivant
        return count

    def sum(self):
        total = 0
        noeud_courant = self.tete
        while noeud_courant is not None:
            total += noeud_courant.valeur
            noeud_courant = noeud_courant.suivant

        return total

def main():
    liste = ListeChainee()
    liste.ajouter_fin(1)
    liste.ajouter_fin(2)
    liste.ajouter_debut(0)
    liste.ajouter_fin(4)
    
    liste.afficher()
    print("-----")
    liste.insert(3,3)
    liste.afficher()

    

    print("Nombre d'éléments :", liste.nb())
    print("Somme des éléments :", liste.sum())

if __name__ == '__main__':
    main()