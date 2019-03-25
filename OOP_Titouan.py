class vehicule():
    def __init__ (self,type, marque, model, couleur):
        self.type=type
        self.marque=marque
        self.model=model
        self.couleur=couleur
        
    def peinture(self,nouvellecouleur):
        self.couleur=nouvellecouleur
    
    def getcouleur(self):
        print(self.couleur)
        

class voiture(vehicule):
    def __init__(self,marque,model,couleur,DA):
        vehicule.__init__(self,'moto',marque,model,couleur)
        self.DA=DA
        
    def getdir(self):
        print('direction assistée?')
        print(self.DA)
        
        
class moto(vehicule):
    def __init__(self,marque,model,couleur,abs):
        vehicule.__init__(self,'moto',marque,model,couleur)
        self.abs=abs
        
    def getabs(self):
        print('abs?')
        print(self.abs)
            
        
mavoiture=vehicule('voiture','peugeot',205,'rouge')
mavoiture.getcouleur()
mavoiture.peinture('rouge vif')
mavoiture.getcouleur()
mamoto=moto('harley','un certain modèle','bleu','non')
mamoto.getabs()
mavoiture2=voiture('porsche',944,'gris','oui')
mavoiture2.getdir()


    