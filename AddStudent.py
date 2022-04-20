from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Student import Student


class AddStudentFrame:
    def __init__(self, frame, table):
        self.add_frame = frame
        self.display_table = table

        self.studclass = Student()
        self.data = self.studclass.data
        self.filename = self.studclass.filename

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.add_name_entry = Entry(self.add_frame, textvariable=self.name, highlightthickness=2,
                                    highlightbackground="#CDAA7D", font=("Lemon/Milk", 10))

        self.add_id_entry = Entry(self.add_frame, textvariable=self.id_no, highlightthickness=2,
                                  highlightbackground="#CDAA7D", font=("Lemon/Milk", 10))
        self.add_year_combo = ttk.Combobox(self.add_frame, textvariable=self.year, font=("Lemon/Milk", 10),
                                           values=[
                                               "1st Year",
                                               "2nd Year",
                                               "3rd Year",
                                               "4th Year",
                                               "5th Year"])
        self.add_course_entry = Entry(self.add_frame, textvariable=self.course, highlightthickness=2,
                                      highlightbackground="#CDAA7D", font=("Lemon/Milk", 10))
        self.add_gender_combo = ttk.Combobox(self.add_frame, textvariable=self.gender, font=("Lemon/Milk", 10),
                                             values=["Male", "Female", "Other"])

        # add_student_interface
        self.add_frame.place(x=20, y=40, width=400, height=410)

        # attributes of the add student feature
        name_label = Label(self.add_frame, text="Name:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        name_label.place(x=20, y=50, width=90, height=40)
        self.add_name_entry.place(x=110, y=50, width=270, height=40)
        id_no_label = Label(self.add_frame, text="ID No.:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        id_no_label.place(x=20, y=120, width=90, height=40)
        name_format = Label(self.add_frame, text="Last Name, First Name, M.I", font=("Tekton Pro", 10), fg="black",
                            bg="white")
        name_format.place(x=115, y=91, height=20)
        self.add_id_entry.place(x=110, y=120, width=270, height=40)
        year_label = Label(self.add_frame, text="Year:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        year_label.place(x=20, y=170, width=90, height=40)
        self.add_year_combo.place(x=110, y=170, width=270, height=40)
        course_label = Label(self.add_frame, text="Course:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        course_label.place(x=20, y=220, width=90, height=40)
        self.add_course_entry.place(x=110, y=220, width=270, height=40)
        gender_label = Label(self.add_frame, text="Gender:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        gender_label.place(x=20, y=270, width=90, height=40)
        self.add_gender_combo.place(x=110, y=270, width=270, height=40)

        # buttons on add student
        add_info_button = Button(self.add_frame, command=self.add_student, text="Add", bg="#CDAA7D", fg="black",
                                 font=("Lemon/Milk", 15))
        add_info_button.place(x=170, y=340, width=90, height=30)
        clear_info_button = Button(self.add_frame, command=self.clear_data, text="Clear", bg="#CDAA7D", fg="black",
                                   font=("Lemon/Milk", 15))
        clear_info_button.place(x=280, y=340, width=90, height=30)

    def clear_data(self):
        self.add_id_entry.delete(0, END)
        self.add_name_entry.delete(0, END)
        self.add_course_entry.delete(0, END)
        self.add_year_combo.delete(0, END)
        self.add_gender_combo.delete(0, END)

    def add_student(self):
        msg = messagebox.askquestion('Add Student', 'Are you sure you want to add the student?')
        if msg == "yes":
            if self.name.get() == "" or self.id_no.get() == "" or self.year == "" or self.course.get() == "" \
                    or self.gender.get() == "":
                messagebox.showerror("Error", "Please fill out all fields")
            elif self.studclass.id_checker(self.id_no.get()):
                if self.id_no.get() in self.data:
                    overwrite = messagebox.askquestion('Overwrite Student', 'ID Number already in database, do you '
                                                                            'wish to overwrite the student information?'
                                                       )
                    if overwrite == "no":
                        return

                self.data[self.id_no.get()] = {'Name': self.name.get().upper(),
                                               'Course': self.course.get().upper(),
                                               'Year': self.year.get(), 'Gender': self.gender.get()}
                self.studclass.data_to_csv()
                messagebox.showinfo("Success!", "Student added to database!")
                self.studclass.display_student_table(self.display_table)
                self.clear_data()
            return
        else:
            return
