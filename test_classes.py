class Vehicule():
    def __init__ (self,type,marque,modele,couleur):
        self.type = type
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
    def peinture(self,nouvelle_couleur):
        self.couleur=nouvelle_couleur

class Moto(Vehicule):
    def __init__ (self,marque,modele,couleur):
        Vehicule.__init__(self,'moto',marque,modele,couleur)
        
    def get_moto(self):
        print ('le vehicule est une moto',self.modele, self.marque, self.couleur)

class Voiture(Vehicule):
    def __init__ (self,marque,modele,couleur,rm,d_ou_e):
        Vehicule.__init__(self,'voiture',marque,modele,couleur)
        self.rm=rm
        self.moteur=d_ou_e
    def get_voiture(self):
        print ('le vehicule est une voiture',self.modele, self.marque, self.couleur,self.rm,self.moteur)

#voiture=Vehicule('voiture','citoen','c3','bleue')
#voiture.get_voiture()
#voiture.peinture('noir')
#voiture.get_voiture()

voiture=Voiture('citoen','c3','bleue',2,'e')
voiture.get_voiture()