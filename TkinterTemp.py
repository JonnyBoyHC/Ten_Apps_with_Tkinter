import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("400x300")

# tkinter variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master=window, text="label", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

# run
window.mainloop()
