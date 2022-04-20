from tkinter import *
from tkinter import messagebox

from Student import Student


class DeleteStudentFrame:
    def __init__(self, frame, table):
        self.delete_frame = frame
        self.display_table = table

        self.stud_class = Student()
        self.data = self.stud_class.data

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()
        self.rows = []
        self.select = False

        # Delete Frame
        self.del_stud_name = Label(self.delete_frame, fg="black", bg="white", font=("Lemon/Milk", 10), anchor='w')
        self.del_stud_id = Label(self.delete_frame, fg="black", bg="white", font=("Lemon/Milk", 10), anchor='w')
        self.del_stud_year = Label(self.delete_frame, fg="black", bg="white", font=("Lemon/Milk", 10), anchor='w')
        self.del_stud_course = Label(self.delete_frame, fg="black", bg="white", font=("Lemon/Milk", 10),
                                     anchor='w')
        self.del_stud_gender = Label(self.delete_frame, fg="black", bg="white", font=("Lemon/Milk", 10),
                                     anchor='w')

        self.delete_frame.place(x=20, y=80, width=400, height=370)
        choose_lbl = Label(self.delete_frame, text="Select Student to Delete", anchor='w', fg="#CDAA7D", bg="white",
                           font=("Tekton Pro", 14))
        choose_lbl.place(x=20, y=10, width=220, height=30)
        choose_stud_btn = Button(self.delete_frame, command=self.select_stud,
                                 text="Select", bg="#CDAA7D", fg="black", font=("Lemon/Milk", 15))
        choose_stud_btn.place(x=280, y=10, width=90, height=30)

        name_label = Label(self.delete_frame, text="Name:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        name_label.place(x=20, y=60, width=90, height=40)
        id_no_label = Label(self.delete_frame, text="ID No.:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        id_no_label.place(x=20, y=110, width=90, height=40)
        year_label = Label(self.delete_frame, text="Year:", font=("Lemon/Milk", 15), bg="#CDAA7D", fg="black")
        year_label.place(x=20, y=160, width=90, height=40)
        course_label = Label(self.delete_frame, text="Course:", font=("Lemon/Milk", 13), bg="#CDAA7D", fg="black")
        course_label.place(x=20, y=210, width=90, height=40)
        gender_label = Label(self.delete_frame, text="Gender:", font=("Lemon/Milk", 13), bg="#CDAA7D", fg="black")
        gender_label.place(x=20, y=260, width=90, height=40)

        delete_button = Button(self.delete_frame, command=self.delete_student, text="Delete", bg="#CDAA7D", fg="black",
                               font=("Lemon/Milk", 15))
        delete_button.place(x=280, y=330, width=90, height=30)

        self.del_stud_name.place(x=115, y=60, width=250, height=40)
        self.del_stud_id.place(x=115, y=110, width=200, height=40)
        self.del_stud_year.place(x=115, y=160, width=200, height=40)
        self.del_stud_course.place(x=115, y=210, width=200, height=40)
        self.del_stud_gender.place(x=115, y=260, width=200, height=40)

    def clear_data(self):
        self.del_stud_name.config(text="")
        self.del_stud_id.config(text="")
        self.del_stud_course.config(text="")
        self.del_stud_year.config(text="")
        self.del_stud_gender.config(text="")

    def delete_student(self):
        if not self.select:
            messagebox.showerror("Error", "Select a student first")
            return
        else:
            msg = messagebox.askquestion('Delete Student', 'Are you sure you want to delete the student?')
            if msg == "yes":
                self.data.pop(self.rows[0], None)
                self.stud_class.data_to_csv()
                messagebox.showinfo("Success!", "Student has been deleted!")
                self.stud_class.display_student_table(self.display_table)
                self.clear_data()

                return
            else:
                return

    def select_stud(self):
        cursor_row = self.display_table.focus()
        contents = self.display_table.item(cursor_row)
        rows = contents['values']

        if rows == "":
            messagebox.showerror("Error", "Select a student first")
            self.select = False
            return
        else:
            self.del_stud_name.config(text=rows[1])
            self.del_stud_id.config(text=rows[0])
            self.del_stud_year.config(text=rows[3])
            self.del_stud_course.config(text=rows[2])
            self.del_stud_gender.config(text=rows[4])
            self.rows = rows
            self.select = True
            return
