import tkinter as tk
from tkinter import messagebox

def set_geometry(root, geometry_string):
    try:
        root.geometry(geometry_string)  
    except tk.TclError:
        # Display an error message if the geometry format is incorrect
        messagebox.showerror("Geometry Error", "Invalid geometry format! Please use WIDTHxHEIGHT format.")

root = tk.Tk()
root.title("Tkinter Window")

#error format
set_geometry(root, "300,200")


root.mainloop()
