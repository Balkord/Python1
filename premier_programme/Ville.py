# EXERCICE FAIRE EN SORTE QU'IL DEMANDE D'ENTREE L'IMMEUBLE, LE NOMBRE D'ETAGE, LE NOM et LE NOMBRE DE BALCON.

# EXERCICE SUIVANT FAIRE UNE INTERFACE GRAPHIQUE DE L'EXO DE AVANT


class Batiment:

    def __init__(self, name, etage, balcon):
        self.name = name
        self.etage = etage
        self.balcon = balcon
        
    
    def get_name(self):
        return self.name
    
    def get_etage(self):
        return self.etage
    
    def get_balcon (self):
        return self.balcon
    

    
class Immeubles(Batiment):
    def __init__(self, name, etage, balcon):
        super().__init__(name, etage, balcon)
        print("Votre batiment s'appelle :" ,name ,"il comporte : ", etage," étages et il possede :", balcon, "balcon")        
        
class Supermarcher(Batiment):
    def __init__(self, name, etage, rayon):
        super().__init__(name, etage, rayon)
        print("Votre supermarcher s'apelle :", name, "il comporte :", etage, "étage et il possede :", rayon, "rayon")

class Banque(Batiment):
    def __init__(self, name, etage, coffre):
        super().__init__(name, etage, coffre)
        print("Votre supermarcher s'apelle :", name, "il comporte :", etage, "étage et il possede :", coffre, "coffre fort !")
        

immeubles1 = Immeubles("bleu", 4 , 5)
immeubles2 = Immeubles("rouge", 5, 5)
immeubles3 = Immeubles
immeubles4 = Immeubles

supermarcher1 = Supermarcher
supermarcher2 = Supermarcher

banque = Banque