# Import
from tkinter import *
# Class Section
class Window1(object):
  def __init__(self):
    self.tk = Tk()
    self.tk.title("Demo Window")
    self.tk.geometry("500x500")
    self.tk.resizable(True, True)
    self.label("Hello World")
    self.tk.mainloop()
    # self.widgets()
    pass
  
  def widgets(self):
    lbl = Label(self.tk, text="Hello")
    lbl.pack()
    pass
  def label(self, text):
    lbl = Label(self.tk, text=text)
    lbl.pack()
    return lbl
    pass
  
win = Window1()
