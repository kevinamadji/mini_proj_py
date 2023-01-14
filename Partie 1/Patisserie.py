class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def display(self):
        print()
        
        
class Image(File):
    def __init__(self, name, size):
        super().__init__(name, size)
    
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self):
        pass 
    
    def post(self, thread, content):
        pass             
    
    def make_thread(self, title, content):
        pass
    

class Moderator(User): 
    def __init__(self, username, password):
        super().__init__(username, password)
            
    def edits(self,post, content):
        pass
    
    def delete(self, thread, post):
        pass
    

class Post:
    def __init__(self, user, time_posted, content):
        self.user = user (User)
        self.time_posted = time_posted
        self.content = content
    
    def display(self):
        pass
    

class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file
        
class Thread:
    def __init__(self, title, time_posted, posts):
        self.title = title
        self.time_posted = time_posted
        self.posts = [Post]
        
    def display(self):
        pass
    
    def add_post(self, post):
        pass
        