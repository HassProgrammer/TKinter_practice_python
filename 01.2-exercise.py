# exercise'''''''''''''''''''''''''''''
# add one more text label and a button with a function that prints 'hello'
#the label should say "my label" and be between the entry widget and the button

import tkinter as tk
from tkinter import ttk

def hello():
    print("Hello")

#create window
window = tk.Tk()
window.geometry("800x500")
window.title("Practice")

entry = ttk.Entry(master=window)
entry.pack()

label =  ttk.Label(master=window, text="My label")
label.pack()

button = ttk.Button(master=window, text="Button", command= hello)
button.pack()

#run
window.mainloop()