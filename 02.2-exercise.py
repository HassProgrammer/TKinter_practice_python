# exercise
# add another button that changes text back to 'some text' and that enables entry

import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()

    label['text'] = entry_text
    entry['state'] = 'disables'

window = tk.Tk()
window.geometry("800x500")
window.title("Getting and setting widget")

label = ttk.Label(master = window, text="Some important text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button_disables = ttk.Button(master=window, text="Disables", command= button_func)
button_disables.pack()


def enable_button_func():
    label['text'] = 'Some important text'

button_enable = ttk.Button(master=window, text="Enable", command= enable_button_func)
button_enable.pack()



window.mainloop()