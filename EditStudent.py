from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Student import Student


class EditStudentFrame:
    def __init__(self, frame, table):
        self.edit_frame = frame
        self.display_table = table

        self.stud_class = Student()
        self.data = self.stud_class.data
        self.filename = self.stud_class.filename

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()
        self.rows = []
        self.select = False

        # Edit
        self.edit_name_entry = Entry(self.edit_frame, textvariable=self.name, highlightthickness=2,
                                     highlightbackground="#CDAA7D", font=("Lemon/Milk", 10))
        self.edit_id_entry = Entry(self.edit_frame, textvariable=self.id_no, highlightthickness=2,
                                   highlightbackground="#CDAA7D", font=("Lemon/Milk", 10))
        self.edit_year_combo = ttk.Combobox(self.edit_frame, textvariable=self.year, font=("Lemon/Milk", 10),
                                            values=[
                                                "1st Year",
                                                "2nd Year",
                                                "3rd Year",
                                                "4th Year",
                                                "5th Year"])
        self.edit_course_entry = Entry(self.edit_frame, textvariable=self.course, font=("Lemon/Milk", 10),
                                       highlightthickness=2, highlightbackground="#CDAA7D")
        self.edit_gender_combo = ttk.Combobox(self.edit_frame, textvariable=self.gender, font=("Lemon/Milk", 10),
                                              values=["Male", "Female", "Other"])

        self.edit_frame.place(x=20, y=40, width=400, height=410)

        # GUI for selecting student to be updated
        choose_label = Label(self.edit_frame, text="Select Student to Edit", anchor='w', fg="#CDAA7D", bg="white",
                             font=("Tekton Pro", 14))
        choose_label.place(x=20, y=48, width=220, height=30)
        choose_stud_btn = Button(self.edit_frame, command=self.select_stud,
                                 text="Select", bg="#CDAA7D", fg="black", font=("Lemon/Milk", 15))
        choose_stud_btn.place(x=280, y=48, width=90, height=30)

        # attributes on edit student feature
        name_format = Label(self.edit_frame, text="Last Name, First Name, M.I", font=("Tekton Pro", 10), fg="#CDAA7D",
                            bg="white")
        name_format.place(x=115, y=141, height=20)
        name_label = Label(self.edit_frame, text="Name:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        name_label.place(x=20, y=100, width=90, height=40)
        self.edit_name_entry.place(x=110, y=100, width=270, height=40)
        id_no_label = Label(self.edit_frame, text="ID No.:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        id_no_label.place(x=20, y=170, width=90, height=40)
        self.edit_id_entry.place(x=110, y=170, width=270, height=40)
        year_label = Label(self.edit_frame, text="Year:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        year_label.place(x=20, y=220, width=90, height=40)
        self.edit_year_combo.place(x=110, y=220, width=270, height=40)
        course_label = Label(self.edit_frame, text="Course:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        course_label.place(x=20, y=270, width=90, height=40)
        self.edit_course_entry.place(x=110, y=270, width=270, height=40)
        gender_label = Label(self.edit_frame, text="Gender:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        gender_label.place(x=20, y=320, width=90, height=40)
        self.edit_gender_combo.place(x=110, y=320, width=270, height=40)

        # buttons for add student feature
        update_info_button = Button(self.edit_frame, command=self.update_student, text="Update", bg="#CDAA7D",
                                    fg="black", font=("Lemon/Milk", 15))
        update_info_button.place(x=170, y=365, width=90, height=30)
        clear_info_button = Button(self.edit_frame, command=self.clear_data, text="Clear", bg="#CDAA7D", fg="black",
                                   font=("Lemon/Milk", 15))
        clear_info_button.place(x=280, y=365, width=90, height=30)

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)

    def update_student(self):
        if not self.select:
            messagebox.showerror("Error", "Select a student first")
            return
        else:
            msg = messagebox.askquestion("Update Student", "Are you sure you want to update the student's information?")
            if msg == "yes":
                if self.name.get() == "" or self.id_no.get() == "" or self.year == "" or self.course.get() == "" \
                        or self.gender.get() == "":
                    messagebox.showerror("Error", "Please fill out all fields")

                elif self.stud_class.id_checker(self.id_no.get()):
                    if self.id_no.get() in self.data and self.id_no.get() != self.rows[0]:
                        overwrite = messagebox.askquestion('Overwrite Student',
                                                           'ID Number already in database, do you '
                                                           'wish to overwrite the student information?'
                                                           )
                        if overwrite == "no":
                            return

                    if self.rows[0] in self.data:
                        self.data[self.rows[0]] = {'Name': self.name.get().upper(),
                                                   'Course': self.course.get().upper(),
                                                   'Year': self.year.get(), 'Gender': self.gender.get()}
                        self.data[self.id_no.get()] = self.data.pop(self.rows[0])
                        self.stud_class.data_to_csv()
                        messagebox.showinfo("Success!", "Student information has been updated!")
                        self.stud_class.display_student_table(self.display_table)
                        self.clear_data()
                return
            else:
                return

    def select_stud(self):
        cursor_row = self.display_table.focus()
        contents = self.display_table.item(cursor_row)
        rows = contents['values']
        self.clear_data()

        if rows == "":
            messagebox.showerror("Error", "Select a student first")
            self.select = False
            return
        else:
            self.edit_name_entry.insert(0, rows[1])
            self.edit_id_entry.insert(0, rows[0])
            self.edit_year_combo.insert(0, rows[3])
            self.edit_course_entry.insert(0, rows[2])
            self.edit_gender_combo.insert(0, rows[4])
            self.rows = rows
            self.select = True
            return
