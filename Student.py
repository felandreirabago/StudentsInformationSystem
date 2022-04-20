import os
import csv
from tkinter import messagebox


class Student:
    def __init__(self):
        self.data = dict()
        self.temp = dict()
        self.filename = 'studentlist.csv'

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w') as csv_file:
                fieldnames = ["ID Number", "Name", "Course", "Year", "Gender"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

        else:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["ID Number"]] = {'Name': row["Name"], 'Course': row["Course"],
                                                   'Year': row["Year"], 'Gender': row["Gender"]}
            self.temp = self.data.copy()

    def data_to_csv(self):
        datalist = []
        with open(self.filename, "w", newline='') as u:
            fieldnames = ["ID Number", "Name", "Course", "Year", "Gender"]
            writer = csv.DictWriter(u, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id_no, stud_details in self.data.items():
                temp = {"ID Number": id_no}
                for key, value in stud_details.items():
                    temp[key] = value
                datalist.append(temp)
            writer.writerows(datalist)

    def display_student_table(self, display_table):
        display_table.delete(*display_table.get_children())
        with open(self.filename, "r", encoding="utf-8") as StudData:
            stud_data = csv.DictReader(StudData)

            for stud in stud_data:
                display_table.insert('', 0, values=(stud['ID Number'], stud['Name'], stud['Course'], stud['Year'],
                                                    stud['Gender']))\


    def id_checker(self, id_num):
        if len(id_num) != 9:
            messagebox.showerror("Error", "Invalid ID Number")
        elif id_num[4] != '-' or not id_num.replace("-", "").isdigit():
            messagebox.showerror("Error", "Invalid ID Number")
        else:
            return True
        return False
