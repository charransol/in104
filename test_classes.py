class Vehicule():
    def __init__ (self,type,marque,modele,couleur):
        self.type = type
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
    def peinture(self,nouvelle_couleur):
        self.couleur=nouvelle_couleur
    def get_voiture(self):
        print ('le vehicule est un',self.type,self.modele, self.marque, self.couleur)

class Moto(Vehicule):
    def __init__ (self,marque,modele,couleur):
        Vehicule.__init__(self,'moto',marque,modele,couleur)
        


class Voiture(Vehicule):
    def __init__ (self,marque,modele,couleur):
        Vehicule.__init__(self,'voiture',marque,modele,couleur)

class Bus(Vehicule):
    def __init__ (self,marque,modele,couleur):
        Vehicule.__init__(self,'bus',marque,modele,couleur)


#voiture=Vehicule('voiture','citoen','c3','bleue')
#voiture.get_voiture()
#voiture.peinture('noir')
#voiture.get_voiture()

voiture=Voiture('citoen','c3','bleue')
voiture.get_voiture()