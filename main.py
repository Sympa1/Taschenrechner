import tkinter
from tkinter import ttk, END

main_window = tkinter.Tk()

ausgabe_label = tkinter.Entry(main_window, width=20, borderwidth=1)
ausgabe_label.grid(row=0, column=0, pady=5, padx=10, sticky="ew")

def button_click(nummer):
    aktuell = ausgabe_label.get()  # Holt den aktuellen Inhalt des Eingabefelds und speichert ihn in einer Variable.
    ausgabe_label.delete(0, END)  # Löscht den aktuellen Inhalt des Eingabefelds. Hier wird der Inhalt ab Index "0" bis zum letzten Eintrag "END" gelöscht. END bezieht sich immer auch den letzten eintag eines Indexes. -> Hier ist der näämlich unbekannt.
    ausgabe_label.insert(0, aktuell + str(nummer))  # Fügt die gedrückte Zahl am Ende des aktuellen Inhalts hinzu. Die "0" gibt den Index an, an dem der neue Text eingefügt werden soll.

def button_clear():
    ausgabe_label.delete(0, END) # Mit dieser Funktion wird der komplette Inhalt des "entry fields" gelöscht. "0" und "END" definieren den zu löschenden Index. "END" nutzen wir da wir nicht im vorfeld wissen wie hoch der Index ist.

def button_komma(): # Die Funktion funktioniert am ende genauso wie die Funktion "button_click". Der punkt wir deingefügt, da es bei Python keine "," bei Floats gibt
    aktuell = ausgabe_label.get()
    ausgabe_label.delete(0, END)
    ausgabe_label.insert(0, aktuell + ".")

def addieren():
    aktuell = ausgabe_label.get() # Holt die aktuell eingegebene Zahl
    global erster_rechenwert  # Definiert eine globale Variable, um die erste Nummer zwischen den Funktionen zu speichern
    global mathe  # Definiert eine globale Variable, um die Art der Operation zu speichern
    mathe = "addieren" # Setzt die Operation auf "addieren". Damit können wir die Operation in einer späterfolgenden Funktion "ergebnis" durchführen
    erster_rechenwert = float(aktuell) # Speichert denv ersten Wert als Datentyp "Float" zum rechnen
    ausgabe_label.delete(0, END)

def subtrahieren():
    aktuell = ausgabe_label.get()
    global erster_rechenwert
    global mathe
    mathe = "subtrahieren"
    erster_rechenwert = float(aktuell)
    ausgabe_label.delete(0, END)

def multiplizieren():
    aktuell = ausgabe_label.get()
    global erster_rechenwert
    global mathe
    mathe = "multiplizieren"
    erster_rechenwert = float(aktuell)
    ausgabe_label.delete(0, END)

def dividieren():
    aktuell = ausgabe_label.get()
    global erster_rechenwert
    global mathe
    mathe = "dividieren"
    erster_rechenwert = float(aktuell)
    ausgabe_label.delete(0, END)

def ergebnis():
    aktuell = ausgabe_label.get() #Holt sich die aktuell eingebene Zahl und speichert sie in "aktuell"
    ausgabe_label.delete(0, END)  # Löscht das Eingabefeld, um Platz für das Ergebnis zu machen. "0" steht für den beginn des Indexes und "END" für das unbekannnte Ende
    if mathe == "addieren": # Prüft ob die Operation "addieren" durchgeführt werden soll
        ergebnis = erster_rechenwert + float(aktuell) # Dies ist der Rechenweg und das Ergebnis wird in der Variable "ergebnis" als float gespeichert
    elif mathe == "subtrahieren": # Das ist die "if else" Anweisung zum subtrahieren
        ergebnis = erster_rechenwert - float(aktuell)
    elif mathe == "multiplizieren": # Das ist die "if else" Anweisung zum multiplizieren
        ergebnis = erster_rechenwert * float(aktuell)
    elif mathe == "dividieren": # Das ist die "if else" Anweisung zum dividieren
        ergebnis = erster_rechenwert / float(aktuell)
    ausgabe_label.insert(0, ergebnis) # Mit insert wird der Wert von "ergebnis" an daas Entry Label "ausgabe_label" übergeben

eingabe_frame = tkinter.LabelFrame(main_window, text="Eingabetasten")
eingabe_frame.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

btn_1 = ttk.Button(eingabe_frame, text="1", command=lambda: button_click(1)) # "lambda" sind sozusagen wegwerf Variablen. Dies ist notwendig, da wir je nach taste einen anderen Parameter/Wert (nummer) übergebeen.
btn_1.grid(row=2, column=0)

btn_2 = ttk.Button(eingabe_frame, text="2", command=lambda: button_click(2))
btn_2.grid(row=2, column=1)

btn_3 = ttk.Button(eingabe_frame, text="3", command=lambda: button_click(3))
btn_3.grid(row=2, column=2)

btn_4 = ttk.Button(eingabe_frame, text="4", command=lambda: button_click(4))
btn_4.grid(row=1, column=0)

btn_5 = ttk.Button(eingabe_frame, text="5", command=lambda: button_click(5))
btn_5.grid(row=1, column=1)

btn_6 = ttk.Button(eingabe_frame, text="6", command=lambda: button_click(6))
btn_6.grid(row=1, column=2)

btn_7 = ttk.Button(eingabe_frame, text="7", command=lambda: button_click(7))
btn_7.grid(row=0, column=0)

btn_8 = ttk.Button(eingabe_frame, text="8", command=lambda: button_click(8))
btn_8.grid(row=0, column=1)

btn_9 = ttk.Button(eingabe_frame, text="9", command=lambda: button_click(9))
btn_9.grid(row=0, column=2)

btn_plus = ttk.Button(eingabe_frame, text="+", command=addieren)
btn_plus.grid(row=3, column=3)

btn_minus = ttk.Button(eingabe_frame, text="-", command=subtrahieren)
btn_minus.grid(row=2, column=3)

btn_mal = ttk.Button(eingabe_frame, text="*", command=multiplizieren)
btn_mal.grid(row=1, column=3)

btn_geteilt = ttk.Button(eingabe_frame, text="/", command=dividieren)
btn_geteilt.grid(row=0, column=3)

btn_ergebnis = ttk.Button(eingabe_frame, text="=", command=ergebnis)
btn_ergebnis.grid(row=3, column= 0)

btn_0 = ttk.Button(eingabe_frame, text="0", command=lambda: button_click(0))
btn_0.grid(row=3, column=1)

btn_komma = ttk.Button(eingabe_frame, text=",", command=button_komma)
btn_komma.grid(row=3, column=2)

btn_clear = ttk.Button(main_window, text="CLEAR", command=button_clear)
btn_clear.grid(row=0, column=1, pady=5, padx=10)

main_window.mainloop()
