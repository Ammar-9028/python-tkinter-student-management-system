from tkinter import *
from tkinter import messagebox
from Admin_Window import Admin_Screen


class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Window")
        self.root.configure(bg="lightblue")
        l1= Label(self.root, text="MMANTC MAIN MENU",font=("Times New Roman", 20),bg="lightblue")
        l1.grid(row=0, column=0,padx=10, pady=10)

        #now ab button banayege

        b1=Button(self.root, text="Admin Login",font=("Times New Roman", 16),fg="white",bg="green",width=20,command=self.admin_login)
        b1.grid(row=1, column=0,padx=10,pady=10,)

        b2=Button(self.root, text="Student Login",font=("Times New Roman", 16),fg="white",bg="green",width=20)
        b2.grid(row=2, column=0,pady=10, padx=10,)

        b3=Button(self.root, text="Exit",font=("Times New Roman", 16),fg="white",bg="orange",width=20, command=self.exit_fun)
        b3.grid(row=3, column=0,pady=10)



    def exit_fun(self):
        ask=messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass
        self.root.mainloop()

    def admin_login(self):
        self.root.withdraw()
        new_window = Toplevel()
        Admin_Screen(new_window,self.root)


