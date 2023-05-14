import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    new_text = entry.get()

    # update the label
    # label.configure(text="some other text")
    label["text"] = new_text
    entry["state"] = "disabled"
    # print(label.configure())


def enable_entry():
    label["text"] = "Some text"
    entry["state"] = "enable"


# create a window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("400x300")

# widgets
label = ttk.Label(master=window, text="Some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="The button", command=button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that enables entry
entry_enable = ttk.Button(master=window, text="enable entry", command=enable_entry)
entry_enable.pack()

# run
window.mainloop()
