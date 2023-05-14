import tkinter as tk
from tkinter import ttk


def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# create a window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("400x300")

# tkinter variable
# string_var = tk.StringVar()
string_var = tk.StringVar(value="start value")

# widgets
label = ttk.Label(master=window, text="label", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

# entry2 = ttk.Entry(master=window, textvariable=string_var)
# entry2.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

# exercise
# create 2 entry fields and 1 labels, they should all be connected via a StringVar
# set a start value of test

exercise_var = tk.StringVar(value="test")

entry1 = ttk.Entry(master=window, textvariable=exercise_var)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable=exercise_var)
entry2.pack()
exercise_label = ttk.Label(master=window, textvariable=exercise_var)
exercise_label.pack()

# run
window.mainloop()
