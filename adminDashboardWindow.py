from tkinter import *
from tkinter import messagebox
from AddStudentWindow import AddStudentScreen
from DeleteStudentWindow import DeleteStudentScreen
from update import Update_Screen
from Search_Student import Search_Screen

class adminDashboardScreen:
    def __init__(self,root,Admin_Screen):
        self.root = root
        self.Admin_Screen = Admin_Screen
        self.root.title("Admin Dashboard Window")
        self.root.resizable(width=True, height=True)
        self.root.config(bg="lightblue")

        #frame for background
        left_frame = Frame(self.root,bg="grey")
        left_frame.grid(row=0,column=0,rowspan=10,columnspan=2,sticky="nsew")

        l6=Label(self.root,text="Admin Dashboard Window",font=("Times New Roman", 20,"bold"),bg="lightblue",fg="black",width=20)
        l6.grid(row=0,column=1,columnspan=6,pady=10, padx=10)
        #for logout button
        b7=Button(self.root,text="Logout",font=("Times New Roman", 16,"bold"), fg="white", bg="red", width=12,command=self.logout)
        b7.grid(row=5,column=0,pady=10, padx=10)
        #Add student button
        b8 = Button(self.root, text="Add Student", font=("Times New Roman", 16,"bold"), fg="white", bg="green", width=12,command=self.open_add_student)
        b8.grid(row=1, column=0, padx=10, pady=10, )
        #Delete button
        b9 = Button(self.root, text="Delete Student", font=("Times New Roman", 16,"bold"), fg="white", bg="green", width=12,command=self.open_delete_student)
        b9.grid(row=2, column=0, pady=10, padx=10, )
        #update student
        b10 = Button(self.root, text="Update Student", font=("Times New Roman", 16,"bold"), fg="white", bg="green", width=12,command=self.open_update_student)
        b10.grid(row=3, column=0, pady=10, padx=10 )
        # Search student
        b12 = Button(self.root, text="Search Student", font=("Times New Roman", 16,"bold"), fg="white", bg="green", width=12,command=self.open_search_student)
        b12.grid(row=4, column=0, pady=10, padx=10)

        # for Exit
        b11 = Button(self.root, text="Exit", font=("Times New Roman", 16), fg="white", bg="orange", width=12,command=self.exit_fun)
        b11.grid(row=6, column=0, pady=10)

        #========now dashboard element========
        #total student
        t_student=Label(self.root,text="Total Student \n 500 ",font=("Times New Roman", 16,"bold"),padx=5, pady=15,bg="#1E293B",fg="white",width=20)
        t_student.grid(row=1, column=4, pady=10,padx=10)
        #male student
        m_student = Label(self.root, text="Male Student \n 300", font=("Times New Roman", 16, "bold"), padx=5, pady=15,bg="grey",fg="white",width=20)
        m_student.grid(row=1, column=5, pady=10, padx=10)
        # female student
        f_student = Label(self.root, text="Female Student \n 200", font=("Times New Roman", 16, "bold"), padx=5, pady=15,bg="#1E293B",fg="white",width=20)
        f_student.grid(row=1, column=6, pady=10, padx=10)
        #FE student
        fe_student = Label(self.root, text="First Year Total Student \n 200", font=("Times New Roman", 16, "bold"), padx=5,pady=15, bg="#1E293B", fg="white", width=20)
        fe_student.grid(row=2, column=4, pady=10, padx=10)
        # male student
        fe_m_student = Label(self.root, text="Male Student \n 300", font=("Times New Roman", 16, "bold"), padx=5, pady=15,bg="grey", fg="white", width=20)
        fe_m_student.grid(row=2, column=5, pady=10, padx=10)
        # female student
        fe_f_student = Label(self.root, text="Female Student \n 200", font=("Times New Roman", 16, "bold"), padx=5,pady=15, bg="#1E293B", fg="white", width=20)
        fe_f_student.grid(row=2, column=6, pady=10, padx=10)

        #SE student
        se_student = Label(self.root, text="Second Year Total Student \n 100", font=("Times New Roman", 16, "bold"), padx=5,pady=15, bg="#1E293B", fg="white", width=20)
        se_student.grid(row=3, column=4, pady=10, padx=10)
        #TE student
        te_student = Label(self.root, text="Third Year Total Student \n 100", font=("Times New Roman", 16, "bold"),padx=5, pady=15, bg="#1E293B", fg="white", width=20)
        te_student.grid(row=4, column=4, pady=10, padx=10)
        #BE student
        be_student = Label(self.root, text="Final Year Total Student \n 100", font=("Times New Roman", 16, "bold"),padx=5, pady=15, bg="#1E293B", fg="white", width=20)
        be_student.grid(row=5, column=4, pady=10, padx=10)
        #total backlog
        back_student = Label(self.root, text="Backlog Total Student \n 50", font=("Times New Roman", 16, "bold"),padx=6, pady=15, bg="#1E293B", fg="white", width=20)
        back_student.grid(row=6, column=4, pady=10, padx=10)



    #NOW AB SAB FUNCTIONS YAHAN :PAR RAHEGE
    def exit_fun(self):
        ask = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass
        self.root.mainloop()


    def logout(self):
        self.root.withdraw()
        self.Admin_Screen.deiconify()


    def open_add_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        AddStudentScreen(new_window,self.root)

    def open_delete_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        DeleteStudentScreen(new_window, self.root)

    def open_update_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Update_Screen(new_window, self.root)

    def open_search_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Search_Screen(new_window, self.root)
