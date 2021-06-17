from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class Lotto:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ithuba National Lottery")
        self.root.geometry("2560x1536")
        self.loader = Image.open("LOTTO BALLS.jpg")
        self.render = ImageTk.PhotoImage(self.loader)
        self.img = Label(self.root, image=self.render)
        self.img.place(x=0, y=0)


        # function
    def logins(self):
        self.log = self.age_entry.get()
        self.log1 = int(self.log)
        if self.log1 < 18:
            messagebox.showerror("NOTE!!", "Not for person under the age of 18")

        else:
            self.root.destroy()
            import lotto_window
            lotto_window.verify()


    def create_widgets(self):
        # labels& entries

        self.head = Label(self.root, text="YOUR TICKET TO MILLIONNERS", font=("bold", 20), bg="green", fg="white")
        self.head.grid(row=0, column=4)

        self.name = Label(text="NAME", fg="black", bg="yellow", font=("bold", 18))
        self.name.place(x=300, y=323)

        self.nm_entry = Entry(width=24, fg="white", bg="black", font=("bold", 18))
        self.nm_entry.place(x=500, y=320)

        self.sname = Label(text="SURNAME", fg="black", bg="yellow", font=("bold", 18))
        self.sname.place(x=300, y=410)

        self.snm_entry = Entry(width=24, fg="white", bg="black", font=("bold", 18))
        self.snm_entry.place(x=500, y=410)

        self.age = IntVar

        self.age_l = Label(text="AGE", fg="black", bg="yellow", font=("bold", 18))
        self.age_l.place(x=300, y=490)

        self.age_entry = Entry(textvariable=self.age, width=12, fg="white", bg="black", font=("bold", 18))
        self.age_entry.place(x=500, y=490)

        # button

        self.btn = Button(self.root, text="LOGIN", bg="green", fg="white", command=self.logins)
        self.btn.place(x=500, y=600)


lotto_app = Lotto()
lotto_app.root.mainloop()
