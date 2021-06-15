
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import rsaidnumber

root = Tk()
root.title("Ithuba National Lottery")
root.geometry("2560x1536")
root.geometry("2560x1536")
loader = Image.open("powerball-jackpot-2048x1365.jpg")
render = ImageTk.PhotoImage(loader)
img = Label(root, image=render)
img.place(x=0, y=0)
loader2 = Image.open("ithuba.jpg")
render2 = ImageTk.PhotoImage(loader2)
img2 = Label(root, image=render2)
img2.place(x=300, y=10)


class Lotto:
    def __init__(self):
        # labels& entries

        self.name = tk.Label(text="FULL NAME", fg="black", bg="green", font=("bold", 18))
        self.name.place(x=300, y=400)

        self.name_entry = Entry(width=24, fg="green", bg="yellow", font=("bold", 18))
        self.name_entry.place(x=500, y=400)

        self.email_l = Label(text="EMAIL ADDRESS", fg="black", bg="green", font=("bold", 18))
        self.email_l.place(x=250, y=452)

        self.snm_entry = Entry(width=24, fg="green", bg="yellow", font=("bold", 18))
        self.snm_entry.place(x=500, y=450)

        self.age_l = Label(text="HOME ADDRESS", fg="black", bg="green", font=("bold", 18))
        self.age_l.place(x=250, y=512)

        self.age_entry = Text(root, width=24, fg="green", bg="yellow", height=6, font=("bold", 18))
        self.age_entry.place(x=500, y=510)

        self.id_no = IntVar()

        self.id_no_l = Label(root, text="ID NUMBER", width=12, fg="black", bg="green", font=("bold", 18))
        self.id_no_l.place(x=250, y=720)

        self.id_entry = Entry(root, textvariable=self.id_no, width=24, fg="green", bg="yellow", font=("bold", 18))
        self.id_entry.place(x=500, y=720)

        # button

        self.btn = Button(root, text="LOGIN", bg="green", fg="white", borderwidth="6")
        self.btn.place(x=400, y=800)

        self.btn = Button(root, text="LOGOUT", bg="green", fg="white", borderwidth="6")
        self.btn.place(x=550, y=800)

        self.btn = Button(root, text="CLOSE", bg="green", fg="white", borderwidth="6", command=Functionality)
        self.btn.place(x=720, y=800)


class Validation(Lotto):
    def __init__(self):
        super(Validation, self).__init__()
        self.id_entry = rsaidnumber.parse(self.id_entry)
        print(self.id_entry.date_of_birth)


class Functionality(Lotto):
    def __init__(self):
        super(Functionality, self).__init__()
        root.destroy()


if __name__ == '__main__':
    lotto_app = Lotto()
    val = Validation()
    root.mainloop()
