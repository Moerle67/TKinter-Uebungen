from tkinter import *

class calculator(object):
    def __init__(self):
        # Hauptfenster
        self.tkFenster = Tk()
        self.tkFenster.title('Rechner')

        #Zahl 1
    
    def buttonPlusClick():
        # Übernahme der Daten
        zahl1 = int(entryZahl1.get())
        zahl2 = int(entryZahl2.get())
        # Verarbeitung der Daten
        ergebnis = zahl1 + zahl2
        # Anzeige der Daten
        labelErgebnis.config(text=str(ergebnis))

    def buttonMinusClick():
        # Übernahme der Daten
        zahl1 = int(entryZahl1.get())
        zahl2 = int(entryZahl2.get())
        # Verarbeitung der Daten
        ergebnis = zahl1 - zahl2
        # Anzeige der Daten
        labelErgebnis.config(text=str(ergebnis))

    def buttonMalClick():
        # Übernahme der Daten
        zahl1 = int(entryZahl1.get())
        zahl2 = int(entryZahl2.get())
        # Verarbeitung der Daten
        ergebnis = zahl1 * zahl2
        # Anzeige der Daten
        labelErgebnis.config(text=str(ergebnis))

    def buttonDurchClick():
        # Übernahme der Daten
        zahl1 = int(entryZahl1.get())
        zahl2 = int(entryZahl2.get())
        # Verarbeitung der Daten
        ergebnis = zahl1 // zahl2
        # Anzeige der Daten
        labelErgebnis.config(text=str(ergebnis))

    def buttonRestClick():
        # Übernahme der Daten
        zahl1 = int(entryZahl1.get())
        zahl2 = int(entryZahl2.get())
        # Verarbeitung der Daten
        ergebnis = zahl1 % zahl2
        # Anzeige der Daten
        labelErgebnis.config(text=str(ergebnis))

