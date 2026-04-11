
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime
import cv2
import os


class AddStudentScreen:
    def __init__(self, root, Add_Screen=None):
        self.root = root
        self.Add_Screen = Add_Screen
        self.root.title("Add Student Here")
        self.root.geometry("1250x750")
        self.root.config(bg="lightblue")

        # --- Variables for Dropdowns/Radio ---
        self.gender_var = StringVar(value="Male")
        self.branch_var = StringVar(value="Select Branch")
        self.category_var = StringVar(value="Select Category")
        self.year_var = StringVar(value="Select Year")
        self.semester_var = StringVar(value="Select Semester")
        self.admission_year_var = StringVar(value="Select Year")

        self.captured_image_raw = None  # To store high-res BGR image for saving

        # --- UI Header ---
        Label(self.root, text="Add Student Window", font=("Times New Roman", 20, "bold"),
              bg="lightblue", fg="black").grid(row=0, column=0, columnspan=10, pady=10)

        # --- Column 1: Student Information ---
        Label(self.root, text="Student Information", font=("Times New Roman", 20, "underline"),
              bg="lightblue", fg="black").grid(row=1, column=0, columnspan=2, pady=10)

        # Name
        Label(self.root, text="Student Name", font=("Times New Roman", 16), bg="lightblue").grid(row=2, column=0,sticky="w", padx=20)
        self.e_name = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_name.grid(row=2, column=1, pady=5)

        # Roll
        Label(self.root, text="Roll Number", font=("Times New Roman", 16), bg="lightblue").grid(row=3, column=0,sticky="w", padx=20)
        self.e_roll = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_roll.grid(row=3, column=1, pady=5)

        # Email
        Label(self.root, text="Email ID", font=("Times New Roman", 16), bg="lightblue").grid(row=4, column=0,
                                                                                             sticky="w", padx=20)
        self.e_email = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_email.grid(row=4, column=1, pady=5)

        # Mobile
        Label(self.root, text="Mobile Number", font=("Times New Roman", 16), bg="lightblue").grid(row=5, column=0,
                                                                                                  sticky="w", padx=20)
        self.e_mobile = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_mobile.grid(row=5, column=1, pady=5)

        # Address
        Label(self.root, text="Enter Address", font=("Times New Roman", 16), bg="lightblue").grid(row=6, column=0,
                                                                                                  sticky="w", padx=20)
        self.e_address = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_address.grid(row=6, column=1, pady=5)

        # PRN
        Label(self.root, text="Enter PRN", font=("Times New Roman", 16), bg="lightblue").grid(row=7, column=0,sticky="w", padx=20)
        self.e_prn = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_prn.grid(row=7, column=1, pady=5)

        # DOB
        Label(self.root, text="Date of Birth", font=("Times New Roman", 16), bg="lightblue").grid(row=8, column=0,
                                                                                                  sticky="w", padx=20)
        self.e_dob = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_dob.grid(row=8, column=1, pady=5)

        # Gender
        Label(self.root, text="Gender", font=("Times New Roman", 16), bg="lightblue").grid(row=11, column=0, sticky="w",
                                                                                           padx=20)
        Radiobutton(self.root, text="Male", variable=self.gender_var, value="Male", bg="lightblue", font=12).grid(
            row=11, column=1, sticky="w")
        Radiobutton(self.root, text="Female", variable=self.gender_var, value="Female", bg="lightblue", font=12).grid(
            row=11, column=1, sticky="e")

        # Branch & Category
        self.create_dropdown("Branch", self.branch_var, ["Computer", "Mechanical", "Civil", "Textile"], 9, 0)
        self.create_dropdown("Category", self.category_var, ["OPEN", "OBC", "SC", "ST", "NT"], 10, 0)

        # --- Column 2: Academic Information ---
        Label(self.root, text="Academic Information", font=("Times New Roman", 20, "underline"),
              bg="lightblue", width=20).grid(row=1, column=6, columnspan=2)

        self.create_dropdown("Year", self.year_var, ["First", "Second", "Third", "Final"], 2, 6)
        self.create_dropdown("Semester", self.semester_var, ["Sem 1", "Sem 2", "Sem 3", "Sem 4"], 3, 6)
        self.create_dropdown("Adm. Year", self.admission_year_var, ["2024", "2025", "2026"], 4, 6)

        Label(self.root, text="Prev % / CGPA", font=("Times New Roman", 16), bg="lightblue").grid(row=5, column=6,
                                                                                                  sticky="w")
        self.e_cgpa = Entry(self.root, width=20, font=("Times New Roman", 16, "bold"))
        self.e_cgpa.grid(row=5, column=7, pady=5)

        # --- Column 3: Photo Section ---
        photo_frame = Frame(self.root, bd=2, relief="ridge", bg="white")
        photo_frame.grid(row=1, column=8, rowspan=11, padx=20, sticky="n")
        photo_frame.config(width=240, height=600)
        photo_frame.grid_propagate(False)

        Label(photo_frame, text="Live Camera", font=("Roboto", 12, "bold"), bg="white").pack(pady=5)
        self.canvas = Canvas(photo_frame, width=200, height=200, bg="lightgray")
        self.canvas.pack()

        # Camera Buttons
        cam_btn_frame = Frame(photo_frame, bg="white")
        cam_btn_frame.pack(pady=10)
        Button(cam_btn_frame, text="Preview", command=self.start_camera, width=9).grid(row=0, column=0, padx=2)
        Button(cam_btn_frame, text="Capture", command=self.capture_image, width=9, bg="orange").grid(row=0, column=1,
                                                                                                     padx=2)

        Label(photo_frame, text="Captured Image", font=("Roboto", 11, "bold"), bg="white").pack(pady=5)
        self.capture_canvas = Canvas(photo_frame, width=200, height=200, bg="white", highlightthickness=1)
        self.capture_canvas.pack()

        # Global Save Button
        self.save_all_btn = Button(photo_frame, text="SAVE FULL RECORD", font=("Roboto", 12, "bold"),
                                   bg="green", fg="white", width=18, command=self.save_full_record)
        self.save_all_btn.pack(pady=20)

    # --- Helper: Dropdown Creator ---
    def create_dropdown(self, label, var, options, r, c):
        Label(self.root, text=label, font=("Times New Roman", 16), bg="lightblue").grid(row=r, column=c, sticky="w",
                                                                                        padx=20)
        menu = OptionMenu(self.root, var, *options)
        menu.config(font=("Times New Roman", 12), width=18)
        menu.grid(row=r, column=c + 1, pady=5)

    # --- Camera Logic ---
    def start_camera(self):
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            messagebox.showerror("Error", "Camera not detected")
            return
        self.show_frame()

    def show_frame(self):
        ret, frame = self.cam.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb).resize((200, 200))
            self.imgtk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.imgtk)
            self.canvas.after(10, self.show_frame)

    def capture_image(self):
        ret, frame = self.cam.read()
        if ret:
            self.captured_image_raw = frame.copy()  # Save BGR for disk storage
            # Display captured image in capture_canvas
            captured_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(captured_rgb).resize((200, 200))
            self.captured_img_tk = ImageTk.PhotoImage(img)
            self.capture_canvas.create_image(0, 0, anchor="nw", image=self.captured_img_tk)
        else:
            messagebox.showwarning("Error", "Failed to capture image")

    # --- Save Logic ---
    def save_full_record(self):
        name = self.e_name.get().strip()
        roll = self.e_roll.get().strip()

        # Validation
        if not name or not roll:
            messagebox.showwarning("Input Error", "Name and Roll Number are required!")
            return
        if self.captured_image_raw is None:
            messagebox.showwarning("Photo Error", "Please capture a student photo first!")
            return

        # Create local directory
        folder = "Student_Database"
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Save Image
        photo_filename = f"{ad}/{roll}_{name.replace(' ', '_')}.jpg"
        cv2.imwrite(photo_filename, self.captured_image_raw)

        # Save Text Data (Log file)
        log_file = f"{folder}/records.txt"
        with open(log_file, "a") as f:
            f.write(
                f"Date: {datetime.now()} | Roll: {roll} | Name: {name} | Branch: {self.branch_var.get()} | Photo: {photo_filename}\n")

        messagebox.showinfo("Success", f"Record for {name} saved successfully!")


if __name__ == "__main__":
    root = Tk()
    obj = AddStudentScreen(root)
    root.mainloop()