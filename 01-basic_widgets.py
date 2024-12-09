import tkinter as tk
# from tkinter import ttk #for using widgets
import ttkbootstrap as ttk #for using widgets

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(f"{km_output}km")

#Window
window = tk.Tk()
# window = ttk.Window(themename= "darkly")
window.title("©️ Ahshanul")
window.geometry("300x150")

#Title
title_label = ttk.Label(master = window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable= entry_int)
button = ttk.Button(master=input_frame, text="Convert", command= convert)
input_frame.pack(pady=10)
entry.pack(side="left", padx = 10)
button.pack(side="left")

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 24", textvariable = output_string)
output_label.pack(pady=10)

# run
window.mainloop()