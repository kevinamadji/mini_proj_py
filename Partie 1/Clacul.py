class Calcul:
    def __init__(self):
        pass
# fonction factorielle    
    def factoriel(self, j):
        f = 1
        for i in range (1, j+1):
            f = f * i
            return f 

# fonction somme     
    def somme(self, n):
        s = 0 
        for m in range (1, n+1):
            s = s + m
        return s
    
# fonction qui calcule les nombres premiers    
    def testPrim(self, nb):
        r = 0
        p = 0
        pe = "est un nombre premier"
        ps = "n'est pas un nombre premier"
        for k in range(2, nb):
            r = nb % k
            if (r == 0):
                p = p + 1
            else:
                p = p 
                
        if (p == 0 ):
            print(pe)
        else:
            print(ps)
    
# fonction liste des diviseur 
    def listDiv(self, nbr):
            l = []
            div = 0
            for a in range(2, nbr):
               div = nbr % a
               if (div == 0):
                   l.append(a) 
            return l
    
    
c = Calcul()

print(c.factoriel(3))
print(c.somme(6))
print(c.testPrim(20))
print(c.listDiv(100))

        
        
        