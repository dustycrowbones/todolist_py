# imported libraries

import tkinter as tk
from tkinter import *
import pickle
import PIL

#HEX code palette: #DAF7A6 #FFC300 #FF5733 #C70039 #900C3F #581845
#please don't mind this HEX list, i just wanted to make this whole thing at least not THAT ugly :c - so i sprinkled in some colors :>

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("Simple To-Do List App")
        
        self.task_list = []
        master.geometry("410x610")

        self.task_label = Label(master, text="Enter Task:", width=12, height=2, bg="#581845", fg="#DAF7A6", font="Courier, 14 bold")
        self.task_label.pack(padx=10, pady=5)

        self.task_entry = Entry(master)
        self.task_entry.pack(padx=5, pady=5)

        self.add_button = Button(master, text="Add Task", command=self.add_task, width=12, height=1, bg = "#FFC300", font="Courier, 12 bold")
        self.add_button.pack(padx=5, pady=5)

        self.delete_button = Button(master, text="Delete Task", command=self.delete_task, width=12, height=1, bg = "#FF5733", font="Courier, 12 bold")
        self.delete_button.pack(padx=5, pady=5)

        self.listbox = Listbox(master, width=50, height=20)
        self.listbox.pack(padx=10, pady=10)

        self.save_button = Button(master, text="Save List", command=self.save_tasks, width=12, height=1, bg = "#C70039", fg="#DAF7A6", font="Courier, 12 bold")
        self.save_button.pack(padx=5, pady=5)

        self.load_button = Button(master, text="Load List", command=self.load_tasks, width=12, height=1, bg = "#900C3F", fg="#DAF7A6", font="Courier, 12 bold")
        self.load_button.pack(padx=5, pady=5)

#definitions (valid attempt?)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.listbox.insert(END, task)
            self.task_entry.delete(0, END)

    def delete_task(self):
        task = self.listbox.get(ACTIVE)
        if task:
            self.listbox.delete(ANCHOR)
            self.task_list.remove(task)

    def save_tasks(self):
        with open("tasks.pickle", "wb") as f:
            pickle.dump(self.task_list, f)

    def load_tasks(self):
        try:
            with open("tasks.pickle", "rb") as f:
                self.task_list = pickle.load(f)
                self.listbox.delete(0, END)
                for task in self.task_list:
                    self.listbox.insert(END, task)
        except FileNotFoundError:
            pass

#root tkinter
root = tk.Tk()

#setting background (hey btw i drew that one myself, based off that HEX palette but wave theme and colors going backwards regarding buttons' colors setting to create higher contrast overall, since i myself have bad vision)
bg_image = tk.PhotoImage(file="window_bkg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#oh right window sizing idk tho if this is important but anyway its here
root.geometry("410x610")

#app part i guess
app = ToDoList(root)

#ok lets make it do something hehee
root.mainloop()

#i hope this is fine. i ended up rolling with more functional thing than that pet idea
# making pet would require base all on GIFs, and that seemed like cheating because it left no room to actually write much code
# I mean program would just play gifs all over again and thats it, booooring :< 
