# Chaque tâche peut avoir une importance différente. Ajouter la possibilité de
# définir des priorités pour une tâche.

import tkinter as tk
import tkinter.messagebox
from Job01 import Task
from Job02 import TaskManager

class MyTaskManagerGUI():
    def getEntry(self):
        title = self.myEntry1.get()
        description = self.myEntry2.get()
        due_date = self.myEntry3.get()
        completed = self.check_state.get()
        priority = self.myEntry4.get()

        # Add the task to the task manager
        self.my_task_manager_list.add(title, description, due_date, completed, priority)


        # Clear the entry fields after adding the task
        self.myEntry1.delete(0, tk.END)
        self.myEntry2.delete(0, tk.END)
        self.myEntry3.delete(0, tk.END)
        #Job04 priority
        self.myEntry4.delete(0, tk.END)

        #show all the items in the list
    def show_tasks(self):
        self.task_display.delete(0, tk.END)
        for task in self.my_task_manager_list.task_list:
            self.task_display.insert(tk.END, task.title)

        #show all the details of the items added to the list with a messagebox
    def show_task_details(self, event):
        # Get the index of the selected item
        index = self.task_display.curselection()
        if index:
            index = int(index[0])
            task = self.my_task_manager_list.task_list[index]
            # Display all the details of the selected task
            if task.completed == 1:
                details = f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\nPriority: {task.priority}\nStatus: Completed"
            else:
                details = f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\nPriority: {task.priority}\nStatus: Uncompleted"

            tk.messagebox.showinfo("Task Details", details)

        #delete the item selected
    def delete_task(self):
        # Get the index of the selected item
        index = self.task_display.curselection()
        if index:
            index = int(index[0])
            # Delete the task from the task manager
            self.my_task_manager_list.delete(index)
            # Remove the task from the listbox
            self.task_display.delete(index)

    def __init__(self, task_manager):
        self.my_task_manager_list = task_manager
        self.root = tk.Tk()
        #label title and entryboxes
        self.label = tk.Label(self.root, text="Welcome to your task Manager", font=("Arial",20))
        self.label.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Title", font=("Arial",10))
        self.label.pack()
        self.myEntry1 = tk.Entry(self.root, width=80)
        self.myEntry1.pack(pady=5)

        self.label = tk.Label(self.root, text="Description", font=("Arial",10))
        self.label.pack()
        self.myEntry2 = tk.Entry(self.root, width=80)
        self.myEntry2.pack(pady=5)

        self.label = tk.Label(self.root, text="Due Date", font=("Arial",10))
        self.label.pack()
        self.myEntry3 = tk.Entry(self.root, width=80)
        self.myEntry3.pack(pady=5)

        #JOB04 menu button for the priority option
        menubutton = tk.Menubutton(self.root, text="Select Option")
        menu = tk.Menu(menubutton, tearoff=False)
        menubutton["menu"] = menu
        menu.add_command(label="1")
        menu.add_command(label="2")
        menu.add_command(label="3")
        menu.add_command(label="4")
        menu.add_command(label="5")
        menubutton.pack()

        '''
        self.label = tk.Label(self.root, text="Priority", font=("Arial",10))
        self.label.pack()
        self.myEntry4 = tk.Entry(self.root, width=80)
        self.myEntry4.pack(pady=5)
        '''

        #check mark to see if a task is complete or not
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Task Completed", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        #organize the buttons on a grid filling all the space
        buttonframe = tk.Frame(self.root)
        buttonframe.pack(fill="x")

        btn1 = tk.Button(buttonframe, text="Add Task", font=("Arial",18), command=self.getEntry)
        btn1.grid(row=0, column=0, padx=10, pady=5)

        btn2 = tk.Button(buttonframe, text="Show Tasks", font=("Arial",18), command=self.show_tasks)
        btn2.grid(row=0, column=1, padx=10, pady=5)

        btn3 = tk.Button(buttonframe, text="Delete Task", font=("Arial",18), command=self.delete_task)
        btn3.grid(row=0, column=2, padx=10, pady=5)

        self.task_display = tk.Listbox(self.root, height=10, width=80)
        self.task_display.pack(pady=10)

        # Bind double click event to show_task_details method
        self.task_display.bind("<Double-Button-1>", self.show_task_details)

        self.root.mainloop()

# Initialize the task manager and the GUI
task_manager = TaskManager() 
MyTaskManagerGUI(task_manager)
