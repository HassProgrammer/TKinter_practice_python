import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Getting and setting widget")
window.geometry("800x500")

def button_func():
    #get the content for the entry
    entry_text = entry.get()

    #update the label
    # label.config(entry_text )
    label['text'] = entry_text


#widgets
label = ttk.Label(master=window, text="Getting and setting widget")
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text="Button", command= button_func)
button.pack()

#run
window.mainloop()