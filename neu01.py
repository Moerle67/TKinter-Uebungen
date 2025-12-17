import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hellow World!")
but1 = tk.Button(root, text="Text ändern")
but2 = tk.Button(root, text="Neues Fenster")
but3 = tk.Button(root, text="Fenster schließen")
but1.pack()
but2.pack()
but3.pack()
label.pack()

root.mainloop()