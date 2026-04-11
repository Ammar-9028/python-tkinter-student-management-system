from tkinter import *
from MenuWindow import MenuScreen

class MainScreen:

    def __init__(self):
        self.root = Tk()
        self.root.title("MMANTC College")
        self.root.resizable(width=False, height=False)
        MenuScreen(self.root)
        self.root.mainloop()

MainScreen()









