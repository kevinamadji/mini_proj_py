class CompteBancaire:
    def __init__(self, numCompte, nom, solde ):
        self.numCompte = numCompte
        self.nom = nom
        self.solde = solde
        
    def Versement(self, montant):
        self.solde = self.solde + montant
    
    def Retrait(self, mr): 
        self.solde = self.solde - mr
        
    def Agio(self):
        self.solde = (self.solde) - (self.solde * 0.05)
        
    def Afficher(self):
        return f"Numero de compte: {self.numCompte}\n Nom: {self.nom}\n Solde: {self.solde} €"
    


C1 = CompteBancaire(125458714, "Amadji kevin", 1000)

C1.Versement(1000)
C1.Retrait(200)
C1.Agio()
print(C1.solde)

print(C1.Afficher())