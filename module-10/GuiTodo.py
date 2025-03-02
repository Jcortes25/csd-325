import tkinter as tk
from tkinter import messagebox

# Function to delete a task
def delete_task(event):
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

# Function to exit the program
def exit_program():
    root.quit()

# Set up the main window
root = tk.Tk()
root.title("Cortes-ToDo")  # Change to your last name

# Create a label
label = tk.Label(root, text="Right-click a task to delete it.")
label.pack(pady=10)

# Create a Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Add a scrollbar to the listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Add menu
menu = tk.Menu(root, background="#ff6347", foreground="#2e8b57")  # Complementary colors
root.config(menu=menu)

# Add File menu with Exit option
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)

# Add a few tasks to the listbox for testing
listbox.insert(tk.END, "Buy groceries")
listbox.insert(tk.END, "Complete homework")
listbox.insert(tk.END, "Clean the house")

# Bind the right-click (Button-3) to delete a task
listbox.bind("<Button-3>", delete_task)

# Run the program
root.mainloop()
