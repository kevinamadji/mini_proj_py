
class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age 
        
    def afficher_nom():
        pass
    
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, classes):
        super().__init__(nom, prenom, age)
        self.classes = classes
               
        

class Prof(Personne):
    def __init__(self, nom, prenom, age, formation):
        super().__init__(nom, prenom, age)
        self.formation = formation 


class GroupEtudiant:
    def __init__(self, groupname, etudiant):
        self.groupname = groupname
        self.etudiants = [etudiant]
        
    def inscrire(self, etudiant):
        self.etudiants.append(etudiant)
    
   
