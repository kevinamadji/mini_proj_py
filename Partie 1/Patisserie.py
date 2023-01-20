from abc import ABC

class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def display(self):
        print()
        
        
class ImageFile(File):
    def display(self):
        print(f"Fichier Image {self.name}")
    
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self):
        print(f"L'utilisateur {self.username} s'est connecter avec succès ")
    
    def post(self, thread, content, file = None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        
        else:
            post = Post(user=self, time_posted= "aujourd'hui", content= content)     
        thread.add_post(post)     
        return post  
    
    def make_thread(self, title, content):
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)


class Moderator(User): 

            
    def edits(self,post, content):
        post.content = content
        
    
    def delete(self, thread, post):
        index = thread.posts.index(post)
        del thread.post[index]
    

class Post:
    def __init__(self, user, time_posted, content):
        self.user = user (User)
        self.time_posted = time_posted
        self.content = content
    
    def display(self):
        print(f"Message posté par {self.user} le {self.time_posted} \n")
        print(self.content)
    

class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file
        
    def display(self):
        super().display()
        print("Pièce joint:")
        self.file.display()
class Thread:
    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]
        
    
    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")
    
    
    def add_post(self, post):
        self.posts.append(post)
        