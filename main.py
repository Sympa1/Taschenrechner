import tkinter
from tkinter import ttk

main_window = tkinter.Tk()

#btn_tkinter = tkinter.Button(main_window, text="Text")
#btn_tkinter.grid(row=0, column=0, padx="5", pady="5")

#btn_ttk = ttk.Button(main_window, text="Text")
#btn_ttk.grid(row=1, column=1, padx="5", pady="5")

ausgabe_label = ttk.Label(main_window, text="Hier wird die Berechnung angeziegt")
ausgabe_label.grid(row=0, column=0)

eingabe_frame = tkinter.LabelFrame(main_window, text="Eingabetasten")
eingabe_frame.grid(row=1, column=0)

btn_1 = ttk.Button(eingabe_frame, text="1")
btn_1.grid(row=2, column=0)

btn_2 = ttk.Button(eingabe_frame, text="2")
btn_2.grid(row=2, column=1)

#btn_3

btn_4 = ttk.Button(eingabe_frame, text="4")
btn_4.grid(row=1, column=0)

main_window.mainloop()