# Chaque tâche peut avoir une importance différente. Ajouter la possibilité de
# définir des priorités pour une tâche.

import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
from tkinter import filedialog
from Job01 import Task
from Job02 import TaskManager
from Job08 import TaskManager
from Job07 import TaskManager

class MyTaskManagerGUI():
    def getEntry(self):
        title = self.myEntry1.get()
        description = self.myEntry2.get()
        due_date = self.myEntry3.get()
        completed = self.check_state.get()
        priority = self.menu_selection.get()

        # Add the task to the task manager
        self.my_task_manager_list.add(title, description, due_date, completed, priority)

        # Clear the entry fields after adding the task
        self.myEntry1.delete(0, tk.END)
        self.myEntry2.delete(0, tk.END)
        self.myEntry3.delete(0, tk.END)
        # Set the check state to false
        self.check_state.set(0)
        #Job04 priority
        self.menu_selection.set("")

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
    
    def update_menubutton_text(self, *args):
        priority = self.menu_selection.get()
        self.menubutton.config(text=f"Priority: {priority}")

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

    #to save tasks in a json
    def save_to_json_callback(self):
        filename = "tasks.json"
        self.my_task_manager_list.save_to_json(filename)
        messagebox.showinfo("Saved", "Tasjs saved to JSON file")

    #to delete all items in a json
    def clear_json_file_callback(self):
        filename = "tasks.json"  # Specify the filename here
        self.my_task_manager_list.clear_json_file(filename)
        messagebox.showinfo("Cleared", "Contents of JSON file cleared.")

    #Job08, to export tasks to csv file
    def export_to_csv_callback(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            self.my_task_manager_list.export_to_csv(filename)
            tk.messagebox.showinfo("Exported", f"Tasks exported to {filename}.")

    #Job07, filter by priority button
    def filter_tasks_by_priority(self):
        # Ask user the priority
        priority = int(input("Enter priority level to filter tasks: "))
        
        # Filter tasks by priority
        filtered_tasks = self.my_task_manager_list.filter_tasks_by_priority(priority)
        
        # Show the filtered tasks
        if filtered_tasks:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks with the specified priority.")



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
        self.menu_selection = tk.StringVar()
        self.menubutton = tk.Menubutton(self.root, text="Select Priority")
        menu = tk.Menu(self.menubutton, tearoff=False)
        self.menubutton["menu"] = menu
        menu.add_command(label="1" , command=lambda: self.menu_selection.set("1"))
        menu.add_command(label="2" , command=lambda: self.menu_selection.set("2"))
        menu.add_command(label="3" , command=lambda: self.menu_selection.set("3"))
        menu.add_command(label="4" , command=lambda: self.menu_selection.set("4"))
        menu.add_command(label="5" , command=lambda: self.menu_selection.set("5"))
        self.menubutton.pack()

        #StringVar() is to store the value of selected priority and update it immediately with update_menubutton_text
        self.menu_selection = tk.StringVar()
        self.menu_selection.trace_add("write", self.update_menubutton_text)
        
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

        btn4 = tk.Button(buttonframe, text="Filtered by Priority", font=("Arial",18), command=self.filter_tasks_by_priority)
        btn4.grid(row=0, column=3, padx=10, pady=5)

        btn5 = tk.Button(buttonframe, text="Save JSON", font=("Arial",18), command=self.save_to_json_callback)
        btn5.grid(row=1, column=0, padx=10, pady=5)

        #Job06
        btn6 = tk.Button(buttonframe, text="Delete JSON", font=("Arial",18), command=self.clear_json_file_callback)
        btn6.grid(row=1, column=1, padx=10, pady=5)


        btn7 = tk.Button(buttonframe, text="Export CSV", font=("Arial",18), command=self.export_to_csv_callback)
        btn7.grid(row=1, column=2, padx=10, pady=5)

        self.task_display = tk.Listbox(self.root, height=10, width=80)
        self.task_display.pack(pady=10)

        # Bind double click event to show_task_details method
        self.task_display.bind("<Double-Button-1>", self.show_task_details)

        self.root.mainloop()

# Initialize the task manager and the GUI
task_manager = TaskManager() 
MyTaskManagerGUI(task_manager)
