from tkinter import *
from tkinter import messagebox

class Update_Screen:
    def __init__(self, root, update_screen):
        self.root = root
        self.update_screen = update_screen
        self.root.title("Admin Login")
        self.root.configure(background="white")
        self.root.resizable(False,False)
        Label(self.root,text="MMANTC Update Student",font=("Century",20,"bold")).grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        # Student ID
        Label(self.root, text="Student ID", bg="white",font=("Roboto", 15, "bold")).grid(row=1, column=0, padx=20, pady=5)
        self.student_id = Entry(self.root, width=35)
        self.student_id.grid(row=1, column=1, pady=5)

        # Student Name
        Label(self.root, text="Student Name", bg="white",font=("Roboto", 15, "bold")).grid(row=2, column=0, padx=20, pady=5)
        self.student_name = Entry(self.root, width=35)
        self.student_name.grid(row=2, column=1, pady=5)

        # Update Button
        Button(self.root, text="Update Student", bg="skyblue", fg="white",
               command=self.open_update_page).grid(row=3, column=1, pady=10)

        self.root.mainloop()

    def open_update_page(self):
        # New Window
        self.update_window = Toplevel(self.root)
        self.update_window.title("Update Student")
        self.update_window.configure(background="white")

        Label(self.update_window, text="New Student ID", bg="white").grid(row=0, column=0, padx=20, pady=5)
        self.new_id = Entry(self.update_window, width=30)
        self.new_id.grid(row=0, column=1, pady=5)

        Label(self.update_window, text="New Student Name", bg="white").grid(row=1, column=0, padx=20, pady=5)
        self.new_name = Entry(self.update_window, width=30)
        self.new_name.grid(row=1, column=1, pady=5)

        Button(self.update_window, text="Save Update", bg="Skyblue", fg="white",
               command=self.save_update).grid(row=2, column=1, pady=10)

    def save_update(self):
        # Yaha actual update logic aayega (database etc.)
        messagebox.showinfo("Updated", "Student Updated Successfully!")
        self.update_window.destroy()
