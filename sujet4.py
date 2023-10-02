class Heure:
    def __init__(self):
        self.__heure = []

    def affichage(self):
        print(self.__heure[0], "Heures", self.__heure[1], "minutes")

    def comparer(self, heure_compare):
        if self.__heure[0] < heure_compare.__heure[0]:
            return -1
        elif self.__heure[0] > heure_compare.__heure[0]:
            return 1
        else:
            if self.__heure[1] < heure_compare.__heure[1]:
                return -1
            elif self.__heure[1] > heure_compare.__heure[1]:
                return 1
            else:
                return 0

class Creneau:
    def __init__(self, heure_debut=Heure(), heure_fin=Heure()):
        self.__heure_debut = heure_debut
        self.__heure_fin = heure_fin

    def affichage(self):
        print("Debut: ", self.__heure_debut._Heure__heure[0], "Heures", self.__heure_debut._Heure__heure[1], "minutes")
        print("Fin: ", self.__heure_fin._Heure__heure[0], "Heures", self.__heure_fin._Heure__heure[1], "minutes")

    def conflictWith(self, creneau_compare):
        if self.__heure_debut._Heure__heure[0] < creneau_compare.__heure_debut._Heure__heure[0] < self.__heure_fin._Heure__heure[0]:
            return True
        elif self.__heure_debut._Heure__heure[0] < creneau_compare.__heure_fin._Heure__heure[0] < self.__heure_fin._Heure__heure[0]:
            return True
        else:
            return False

    def duree(self):
        return ((self.__heure_fin._Heure__heure[0] - self.__heure_debut._Heure__heure[0]) * 60) + (self.__heure_fin._Heure__heure[1] - self.__heure_debut._Heure__heure[1])

class Planning:
    def __init__(self):
        self.__creneaux = []

    def ajouterCreneau(self, creneau):
        self.__creneaux.append(creneau)

    def dureeTotale(self):
        duree = 0
        for creneau in self.__creneaux:
            duree += creneau.duree()
        return "Duree totale: " + str(duree) + " minutes"

def main():
    heure1 = Heure()
    heure1._Heure__heure = [10, 30]

    heure2 = Heure()
    heure2._Heure__heure = [10, 40]

    heure3 = Heure()
    heure3._Heure__heure = [12, 30]

    heure4 = Heure()
    heure4._Heure__heure = [12, 40]

    creno1 = Creneau(heure1, heure2)
    creno2 = Creneau(heure3, heure4)
    
    planning1 = Planning()
    planning1.ajouterCreneau(creno1)
    planning1.ajouterCreneau(creno2)
    print(planning1.dureeTotale())

main()
