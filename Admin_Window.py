from tkinter import *
from tkinter import messagebox
from adminDashboardWindow import *

class MainScreen:
    def __init__(self):
        self.root = Tk()


class Admin_Screen:
    def __init__(self,root,Menu_Screen):
        self.root = root
        self.Menu_Screen = Menu_Screen
        self.root.title("Admin Screen")
        self.root.configure(background="lightblue")

        self.username = StringVar()
        self.password = StringVar()


        l3 = Label(self.root, text="Admin Screen", font=("Times New Roman", 18,"bold"),bg="lightblue")
        l3.grid(row=0, column=0)
        #for username
        l4 = Label(self.root, text="Enter Username", font=("Times New Roman", 16,"bold"), fg="black",bg="lightblue")
        l4.grid(row=1, column=0)
        e4 = Entry(self.root,width=20,font=("Times New Roman", 16,"bold"),fg="black",textvariable=self.username)
        e4.grid(row=1, column=1, pady=10, padx=10,columnspan=2)
        #for password
        l5 = Label(self.root, text="Enter Password", font=("Times New Roman", 18, "bold"), fg="black",bg="lightblue")
        l5.grid(row=2, column=0)
        e5 = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"), fg="black", textvariable=self.password)
        e5.grid(row=2, column=1, pady=10, padx=10, columnspan=2)
        #for exit button
        b5=Button(self.root,text="Login",font=("Times New Roman", 18, "bold"),fg="black",bg="green",width=8,command=self.check_login)
        b5.grid(row=3,column=0,pady=10,padx=10)
        #for go back button
        b6 = Button(self.root, text="Go Back", font=("Times New Roman", 18, "bold"), fg="black",bg="green", width=8,command=self.go_back)
        b6.grid(row=3, column=1, pady=10, padx=10)
        #for Exit
        b7 = Button(self.root, text="Exit", font=("Times New Roman", 18, "bold"), fg="black",bg="red", width=8)
        b7.grid(row=3, column=2, pady=10, padx=10)

        self.root.mainloop()


    def go_back(self):
        self.root.destroy()
        self.Menu_Screen.deiconify()

    def check_login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error","Please enter both username and password")
        else:
            if self.username.get() == "admin" or self.password.get() == "1234":
                self.root.destroy()
                new_window = Toplevel()
                adminDashboardScreen(new_window,self.root)

            else:
                messagebox.showerror("Error","Please enter both username and password")



