from tkinter import *
from tkinter import messagebox

class DeleteStudentScreen:
    def __init__(self, root, Delete_Screen=None):
        self.root = root
        self.Delete_Screen = Delete_Screen
        self.root.title(" Delete Student Here ")
        self.root.resizable(width=True, height=True)
        self.root.config(bg="lightblue")

        l7 = Label(self.root, text="Delete Student Window", font=("Times New Roman", 20), bg="lightblue", fg="black",width=20)
        l7.grid(row=0, column=4, columnspan=5, pady=10, padx=10)
        Button(self.root, text="Back", font=("Times New Roman", 18), command=self.go_back).grid(row=7, column=1,pady=10)



       #search name
        Label(self.root, text="Student Name", font=("Times New Roman", 16), bg="lightblue").grid(row=1, column=0,sticky="w", padx=20)
        self.e_name = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_name.grid(row=1, column=1, pady=5)

        # Roll
        Label(self.root, text="Roll Number", font=("Times New Roman", 16), bg="lightblue").grid(row=2, column=0,sticky="w", padx=20)
        self.e_roll = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_roll.grid(row=2, column=1, pady=5)

        # PRN
        Label(self.root, text="Enter PRN", font=("Times New Roman", 16), bg="lightblue").grid(row=3, column=0,sticky="w", padx=20)
        self.e_prn = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_prn.grid(row=3, column=1, pady=5)

    def go_back(self):
        self.root.destroy()
        self.Delete_Screen.deiconify()