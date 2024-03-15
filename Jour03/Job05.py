# Modifier la classe “taskManager” afin d'intégrer une méthode à votre classe
# permettant de sauvegarder les tâches dans un fichier JSON. Ajouter toutes
# les méthodes nécessaires à la manipulation de ce JSON.

from Job01 import Task
import json

class TaskManager():
    
    '''def __init__(self, title, description, due_date, completed):
        super().__init__(title, description, due_date, completed)
        #self.tasks = []'''
    
    
    def __init__(self):
        self.task_list = []
       
    def add(self,title, description, due_date, completed):
        new_task = Task(title, description, due_date, completed)
        self.task_list.append(new_task)
        #print("Task added:", new_task)
        
    def delete(self, index):
        if 0 <= index < len(self.task_list):
            deleted_task = self.task_list[index]
            del self.task_list[index]
            #print("Task deleted:", deleted_task)
        else:
            print("Invalid task index.")

    def show(self):
        if self.task_list:
            print("Tasks:")
            index = 0
            for task in self.task_list:
                index += 1
                print(str(index) + " --> " + str(task))

        else:
            print("No tasks available.")

task_manager = TaskManager() 
#task_manager.add("Write CV", "Write CV for Soft Skill class", "18/03/2024", False)
#task_manager.add("Do Python exercises", "Finish all jobs of Day2", "17/03/2024", True)
#task_manager.show()
#task_manager.delete(1)
#task_manager.show()
