import customtkinter as ctk

def add_task():
    task = task_entry.get()
    if task:  
        task_label = ctk.CTkLabel(scrollable_frame, text=task)
        task_label.pack()
        task_label.bind("<Button-1>", lambda event, label=task_label: select_task(label)) 
        tasks[task_label] = task  
        task_entry.delete(0, ctk.END)

def select_task(label):
    
    global selected_task
    if selected_task:  
        selected_task.configure(fg_color="transparent")  
    selected_task = label
    selected_task.configure(fg_color="gray") 

def delete_task():
    global selected_task
    if selected_task:
        tasks.pop(selected_task, None)  
        selected_task.destroy()  
        selected_task = None  

root = ctk.CTk()
root.geometry("750x450")
root.resizable(False, False)
root.title("To-Do List")
root.iconbitmap("vector-checklist-icon.ico")

tasks = {}  
selected_task = None  

title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(pady=(20, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=600, height=300)
scrollable_frame.pack()

task_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Enter Task Here")
task_entry.pack(fill="x")

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

add_button = ctk.CTkButton(button_frame, text="Add", width=250, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = ctk.CTkButton(button_frame, text="Delete", width=250, command=delete_task, fg_color="red", hover_color="darkred")
delete_button.grid(row=0, column=1, padx=5)

root.mainloop()
