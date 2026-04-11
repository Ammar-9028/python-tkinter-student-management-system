# from tkinter import *
# from tkinter import messagebox
#
# class Search_Screen:
#     def __init__(self, root, search_screen):
#         self.root = root
#         self.search_screen = search_screen
#         self.root.title("Admin Login Search")
#         self.root.configure(background="white")
#         Label(self.root,text="MMANTC Search Student",font=("Century",20,"bold")).grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#         Label(self.root, text="Student ID", bg="white",font=("Roboto", 15, "bold")).grid(row=1, column=0, sticky="w", padx=20, pady=5)
#         self.student_id = Entry(self.root, width=40)
#         self.student_id.grid(row=1, column=1, pady=5)
#
#         Label(self.root, text="Student Name", bg="white",font=("Roboto", 15, "bold")).grid(row=2, column=0, sticky="w", padx=20, pady=5)
#         self.student_name = Entry(self.root, width=40)
#         self.student_name.grid(row=2, column=1, pady=5)
#
#         Button(self.root, text="Search Student", bg="red", fg="white",
#                command=self.search_student).grid(row=3, column=1, pady=10)
#
#         self.root.mainloop()
#
#     def search_student(self):
#         self.student_id.delete(0, END)
#         self.student_name.delete(0, END)
#         messagebox.showinfo("Success", "Student Searched Successfully!")

from tkinter import *
from tkinter import messagebox

class Search_Screen:
    def __init__(self, root, search_screen):
        self.root = root
        self.search_screen = search_screen

        self.root.title("Search Student")
        self.root.state("zoomed")   # Full screen
        self.root.config(bg="#E0F7FA")

        # ===== HEADER =====
        header = Frame(self.root, bg="#0d47a1", height=60)
        header.pack(fill=X)

        Label(header,
              text="MMANTC - Search Student",
              font=("Century", 22, "bold"),
              bg="#0d47a1",
              fg="white").pack(pady=10)

        # ===== MAIN FRAME =====
        main_frame = Frame(self.root, bg="#E0F7FA")
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # ===== LEFT FRAME (INPUT) =====
        left_frame = Frame(main_frame, bg="white", bd=2, relief="ridge")
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(left_frame,
              text="Search Filters",
              font=("Roboto", 18, "bold"),
              bg="white").pack(pady=20)

        # Student ID
        Label(left_frame, text="Student ID", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.student_id = Entry(left_frame, width=30, font=("Roboto", 12))
        self.student_id.pack(padx=20, pady=5)

        # Name
        Label(left_frame, text="Student Name", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.student_name = Entry(left_frame, width=30, font=("Roboto", 12))
        self.student_name.pack(padx=20, pady=5)

        # Course
        Label(left_frame, text="Course", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.course = Entry(left_frame, width=30, font=("Roboto", 12))
        self.course.pack(padx=20, pady=5)

        # Year
        Label(left_frame, text="Year", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.year = Entry(left_frame, width=30, font=("Roboto", 12))
        self.year.pack(padx=20, pady=5)

        # Buttons
        btn_frame = Frame(left_frame, bg="white")
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Search",
               bg="#0d47a1",
               fg="white",
               font=("Roboto", 12, "bold"),
               width=12,
               command=self.search_student).grid(row=0, column=0, padx=10)

        Button(btn_frame,
               text="Clear",
               bg="gray",
               fg="white",
               font=("Roboto", 12, "bold"),
               width=12,
               command=self.clear_fields).grid(row=0, column=1, padx=10)

        # ===== RIGHT FRAME (RESULT DISPLAY) =====
        right_frame = Frame(main_frame, bg="white", bd=2, relief="ridge")
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(right_frame,
              text="Student Details",
              font=("Roboto", 18, "bold"),
              bg="white").pack(pady=20)

        self.result_box = Label(right_frame,
                                text="Search result will appear here",
                                font=("Roboto", 14),
                                bg="#F5F5F5",
                                width=40,
                                height=12,
                                relief="sunken",
                                anchor="nw",
                                justify=LEFT)

        self.result_box.pack(padx=20, pady=20)

        # Back Button
        Button(right_frame,
               text="Back",
               bg="#757575",
               fg="white",
               font=("Roboto", 12),
               command=self.go_back).pack(pady=10)

    # ===== FUNCTIONS =====

    def search_student(self):
        sid = self.student_id.get()
        name = self.student_name.get()

        if sid == "" and name == "":
            messagebox.showwarning("Input Error", "Enter at least ID or Name")
            return

        # 🔹 Dummy data (replace with database later)
        result = f"""
Student ID: {sid if sid else "101"}
Name: {name if name else "Faisal"}
Course: B.Tech CSE
Year: 2nd Year
DOB: 01/01/2005
Status: Active
"""

        self.result_box.config(text=result)

    def clear_fields(self):
        self.student_id.delete(0, END)
        self.student_name.delete(0, END)
        self.course.delete(0, END)
        self.year.delete(0, END)

        self.result_box.config(text="Search result will appear here")

    def go_back(self):
        self.root.destroy()
        self.search_screen.deiconify()
