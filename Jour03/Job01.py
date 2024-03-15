# Créer une classe nommée “Task” avec les attributs privés suivants :
# ➔ “title”
# ➔ “description”
# ➔ “due_date”
# ➔ “completed”

# Ajouter des méthodes afin de pouvoir manipuler ses attributs.

class Task():
    def __init__(self, title, description, due_date, completed):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date {self.due_date}, Completed {self.completed}"

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_due_date(self):
        return self.due_date
    
    def get_completed(self):
        return self.completed
    
    def set_title(self, x):
        self.title = x
    
    def set_description(self, x):
        self.description = x
    
    def set_due_date(self, x):
        self.due_date = x
    
    def set_completed(self, x):
        self.completed = x
    
    