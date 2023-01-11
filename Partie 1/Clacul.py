class Calcul:
    def __init__(self):
        pass
    
    def factoriel(self, n):
        f = 1
        n = i = 1
        while(i< n):
            f = f * i
            i = i+1
        return f
    
c = Calcul()

print(c.factoriel(5))
        
        
        