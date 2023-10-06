
class Expression:
    def evaluer(self, contexte):
        pass

class Constante(Expression):
    def __init__(self, valeur):
        self.valeur = valeur
    
    def evaluer(self, contexte):
        return self.valeur

class OperateurBinaire(Expression):
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

class Plus(OperateurBinaire):
    def evaluer(self, contexte):
        return self.gauche.evaluer(contexte) + self.droite.evaluer(contexte)

class Moins(OperateurBinaire):
    def evaluer(self, contexte):
        return self.gauche.evaluer(contexte) - self.droite.evaluer(contexte)

class Multiplier(OperateurBinaire):
    def evaluer(self, contexte):
        return self.gauche.evaluer(contexte) * self.droite.evaluer(contexte)

class Diviser(OperateurBinaire):
    def evaluer(self, contexte):
        droite_valeur = self.droite.evaluer(contexte)
        if droite_valeur == 0:
            raise ValueError("Division par zéro")
        return self.gauche.evaluer(contexte) / droite_valeur

class Variable(Expression):
    def __init__(self, nom):
        self.nom = nom

    def evaluer(self, contexte):
        return contexte.get_valeur(self.nom)

class Contexte:
    def __init__(self):
        self.variables = {}

    def associer_variable(self, nom, valeur):
        self.variables[nom] = valeur

    def get_valeur(self, nom):
        if nom in self.variables:
            return self.variables[nom]
        else:
            raise KeyError(f"La variable '{nom}' n'a pas été définie dans le contexte")


contexte = Contexte()
contexte.associer_variable('x', 5)
contexte.associer_variable('y', 3)

exp = Plus(Constante(2), Multiplier(Variable('x'), Variable('y')))
resultat = exp.evaluer(contexte)
print(resultat)
