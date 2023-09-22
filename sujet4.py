class Heure:
    # La classe heure
    def __init__(self, heure=list):
        self.__heure = heure
    
    def affichage(self):
        print( self.__heure[0],"Heures", self.__heure[1],"minutes")
    
    def comparer(self, heure_compare):
        
        if self.__heure[0] < heure_compare[0]:
            return -1
        elif self.__heure[0] > heure_compare[0]:
            return 1
        else:
            if self.__heure[1] < heure_compare[1]:
                return -1
            elif self.__heure[1] > heure_compare[1]:
                return 1
            else:
                return 0
    
        
heure = Heure([14,52])
heure.affichage()
print(heure.comparer([14,50]))
