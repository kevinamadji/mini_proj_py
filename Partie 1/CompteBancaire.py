class CompteBancaire:
    def __init__(self, numCompte, nom, solde ):
        self.numCompte = numCompte
        self.nom = nom
        self.solde = solde
        
    def Versement(self, montant):
        self.solde = self.solde + montant
    
    def Retrait(self, mr):
        if(self.solde < 0):
            print("Impossible de faire un retrait car solde inssufisant") 
        else:
           self.solde = self.solde - mr 
        
        
    def Agio(self):
        self.solde = (self.solde) - (self.solde * 0.05)
        
    def Afficher(self):
        return f"Numero de compte: {self.numCompte}\n Nom: {self.nom}\n Solde: {self.solde} €"





class Book:
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price
    
    def View(self):
        return f"Tittre: {self.Title}\nAuteur: {self.Author}\nPrix: {self.Price}€"





class Rectangle:
    def __init__(self, long, larg):
        self.long = long
        self.larg = larg
    
    def Perimetre(self):
        return (self.larg + self.long)*2
    
    def Surface(self):
        return self.long * self.larg
    
    def getLong(self):
        return self.long
    
    def setLong(self, lo):
        self.long = lo
    
    def getLarg(self):
        return self.larg
    
    def setLarg(self, la): 
        self.larg = la


class Parallelepipede(Rectangle):
    def __init__(self, long, larg, hauteur):
        super().__init__(long, larg)
        self.hauteur = hauteur
    
    def Volume(self):
        return self.larg * self.long * self.hauteur
        
    


print("************************************TEST**********************************************************")
C1 = CompteBancaire(125458714, "Amadji kevin", 1000)
C1.Versement(1000)
C1.Retrait(200)
C1.Agio()
print(C1.solde)
print(C1.Afficher())

print("************************************TEST**********************************************************")
book1 = Book("Le médecin imaginaire ", "Molière", 29)
print(book1.View())

print("************************************TEST**********************************************************")
r = Rectangle(20, 15)
print(r.Perimetre())
print(r.Surface())
r.setLarg(5)
r.setLong(10)
print(r.getLong())
print(r.getLarg())

print("************************************TEST**********************************************************")
p = Parallelepipede(10, 5, 2)
print(p.Volume())