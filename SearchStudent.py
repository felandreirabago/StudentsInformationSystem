from tkinter import *
from tkinter import ttk

from Student import Student


class SearchStudentFrame:
    def __init__(self, frame):
        self.search_frame = frame

        self.studclass = Student()
        self.data = self.studclass.data
        self.filename = self.studclass.filename

        # Search
        self.search_bar_entry = Entry(self.search_frame, highlightthickness=2, highlightbackground="#CDAA7D",
                                      font=("Lemon/Milk", 12))
        self.srch_btn_img = PhotoImage(file=r"search_button_img.png")
        self.srch_result_msg = Label(self.search_frame, text="", bg="white", fg="#CDAA7D", font=("Tekton Pro", 12))
        self.search_result_frame = Frame(self.search_frame, bg="white", highlightthickness=2,
                                         highlightbackground="#CDAA7D")
        scrll_x = Scrollbar(self.search_result_frame, orient=HORIZONTAL)
        self.results_table = ttk.Treeview(self.search_result_frame, xscrollcommand=scrll_x.set,
                                          columns=("name", "course", "year", "gender"))

        scrll_x.pack(side=BOTTOM, fill=X)
        scrll_x.config(command=self.results_table.xview)
        self.results_table.heading("name", text="Name")
        self.results_table.heading("course", text="Course")
        self.results_table.heading("year", text="Year")
        self.results_table.heading("gender", text="Gender")
        self.results_table['show'] = 'headings'
        self.results_table.column("name", width=140)
        self.results_table.column("course", width=60)
        self.results_table.column("year", width=60)
        self.results_table.column("gender", width=50)

        self.srchrslts_label = Label(self.search_frame, text="  Search Result", anchor='w', bg="#CDAA7D", fg="black",
                                     font=("Lemon/Milk", 13))

        self.search_frame.place(x=20, y=80, width=400, height=370)
        id_no_label = Label(self.search_frame, text="ID #", bg="#CDAA7D", fg="black", font=("Lemon/Milk", 15))
        id_no_label.place(x=30, y=25, width=50, height=40)
        self.search_bar_entry.place(x=80, y=25, width=250, height=40)
        search_button = Button(self.search_frame, command=self.search_student,
                               image=self.srch_btn_img, bg="#CDAA7D", fg="black", font=("Lemon/Milk", 15))
        search_button.place(x=330, y=25, width=40, height=40)

        self.cover = Frame(self.search_frame, bg="white")

        self.cover.place(x=30, y=70, width=340, height=300)
        self.search_bar_entry.delete(0, END)

    def search_student(self):
        if self.studclass.id_checker(self.search_bar_entry.get()):
            self.srch_result_msg.place(x=30, y=80, height=20, width=100)
            self.cover.place_forget()

            if self.search_bar_entry.get() in self.data:
                stud = list(self.data[self.search_bar_entry.get()].values())
                self.results_table.delete(*self.results_table.get_children())
                self.srch_result_msg.config(text="1 record found")
                self.srchrslts_label.place(x=30, y=110, width=340, height=35)
                self.search_result_frame.place(x=30, y=140, width=340, height=200)
                self.results_table.insert('', 'end', values=[stud[0], stud[1], stud[2], stud[3]])
                self.results_table.pack(fill=BOTH, expand=1)
                return
            else:
                self.srchrslts_label.place_forget()
                self.search_result_frame.place_forget()
                self.srch_result_msg.config(text="No records found")
                return
        return
