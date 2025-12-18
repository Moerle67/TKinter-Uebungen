import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hellow World!")

def text_aendern():
    label.config(text="Bye")

def neues_fenster():
    root2 = tk.Tk()
    label2 = tk.Label(root2, text="zweites Fenster")
    label2.pack()
    root2.mainloop()

def fenster_schließen():
    root.destroy()

but1 = tk.Button(root, text="Text ändern", command=text_aendern)
but2 = tk.Button(root, text="Neues Fenster", command=neues_fenster)
but3 = tk.Button(root, text="Fenster schließen", command=fenster_schließen)
label.pack()
but1.pack()
but2.pack()
but3.pack()

root.mainloop()