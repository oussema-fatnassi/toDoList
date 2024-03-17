# Ajouter une méthode permettant d’afficher les tâches filtrées en fonction de
# leur importance.

from Job01 import Task
import json
import os

class TaskManager():
    
    def __init__(self):
        self.task_list = []
       
    def add(self,title, description, due_date, completed, priority):
        new_task = Task(title, description, due_date, completed, priority)
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
            
    # open a file in write mode, convert each task to a dictionary and write them to the file using "json.dump()"
    def save_to_json( self, filename):
        with open (filename, 'w') as f:
            json.dump([task.to_dict() for task in self.task_list], f, indent="3")
            
    # open a file in read mode, loads the json data from the file using 'json.load()', convert each dictionary back to a Task object and store them in 'task_list'
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        self.task_list = [Task(**task_data) for task_data in data] #task data is a dictionary created by json to store the information about the tasks

    #Job06
    #clears all tasks from task_list
    def clear_json_file(self, filename):
        # Vérifie si le fichier existe
        if os.path.exists(filename):
            # Ouvre le fichier en mode écriture pour le vider
            with open(filename, 'w') as json_file:
                json_file.write('')

    #Job07, if the task has the same priority given, then return the list of tasks
    def filter_tasks_by_priority(self, priority):
        filtered_tasks = []
        for task in self.task_list:
            if task.priority == priority:
                filtered_tasks.append(task)
        return filtered_tasks
   
task_manager = TaskManager() 
#task_manager.add("Write CV", "Write CV for Soft Skill class", "18/03/2024", False)
#task_manager.add("Do Python exercises", "Finish all jobs of Day2", "17/03/2024", True)
#task_manager.show()
#task_manager.delete(1)
#task_manager.show()

