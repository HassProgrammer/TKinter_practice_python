import tkinter as tk
from tkinter import ttk

def button_function():
    print("A button was pressed")

#create a window
window = tk.Tk()
window.title("Window & Widgets")
window.geometry("800x500")

#ttk widgets / ttk label
label_text = ttk.Label(master = window, text = "This is just a test")
label_text.pack()

#Create  widgets / tk text
text_box = tk.Text(master = window)
text_box.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#ttk button
button = ttk.Button(master=window, text= "A button", command = button_function)
button.pack()
#run
window.mainloop()
# print("Hello")