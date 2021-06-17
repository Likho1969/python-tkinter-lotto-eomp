
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
    def __init__(self, window):
        # labels& entries

        self.name = tk.Label(window, text="FULL NAME", fg="black", bg="green", font=("bold", 18))
        self.name.place(x=300, y=400)

        self.name_entry = Entry(window, width=24, fg="green", bg="yellow", font=("bold", 18))
        self.name_entry.place(x=500, y=400)

        self.email_l = Label(window, text="EMAIL ADDRESS", fg="black", bg="green", font=("bold", 18))
        self.email_l.place(x=250, y=452)

        self.email_entry = Entry(window, width=24, fg="green", bg="yellow", font=("bold", 18))
        self.email_entry.place(x=500, y=450)

        self.address_l = Label(window, text="HOME ADDRESS", fg="black", bg="green", font=("bold", 18))
        self.address_l.place(x=250, y=512)

        self.address_entry = Text(window, width=24, fg="green", bg="yellow", height=6, font=("bold", 18))
        self.address_entry.place(x=500, y=510)

        self.id_no = IntVar()

        self.id_no_l = Label(window, text="ID NUMBER", width=12, fg="black", bg="green", font=("bold", 18))
        self.id_no_l.place(x=250, y=720)

        self.id_entry = Entry(window, textvariable=self.id_no, width=24, fg="green", bg="yellow", font=("bold", 18))
        self.id_entry.place(x=500, y=720)

        # button

        self.btn = Button(window, text="LOGIN", bg="green", fg="white", borderwidth="6", command=self.id_check)
        self.btn.place(x=400, y=800)

        self.btn = Button(window, text="LOGOUT", bg="red", fg="white", borderwidth="6", command=self.close)
        self.btn.place(x=550, y=800)

        self.btn = Button(window, text="CLEAR", bg="green", fg="white", borderwidth="6", command=self.clear)
        self.btn.place(x=720, y=800)

    def id_check(self):
        try:
            self.id_no = int(self.id_entry.get())
            self.id_ls = self.id_entry.get()

            self.year = self.id_entry.get()
            self.year2 = self.id_entry.get()

            if type(self.id_no) == type(str()) or len(self.id_ls) != 13:
                raise ValueError
            elif int(self.year) <= 3:

                messagebox.showinfo(title="Play!", message="Lets Play!")
                root.destroy()
                import win
            elif int(self.year2) > 3 and int(self.year2) > 21:
                messagebox.showinfo(title="Grab Your Millions", message="Are You Ready!! Let's dive in and Play!!")
                root.destroy()
                import win
            else:
                messagebox.showinfo(title="Under Age", message="Your are too young to play")
        except ValueError:

            messagebox.showerror(title="Invalid Id", message="Please enter valid ID")
            self.id_entry.delete(0, END)

    def details(self):
        self.name = self.name_entry.get()
        self.email = str(self.email_entry.get())

        if "@" in self.email_entry.get():
            messagebox.showinfo("Email Address", "Correct Email")

        else:
            messagebox.showinfo(title='Alert!', message="Please enter valid email address!")
            self.email_entry.delete(0, END)

    def close(self):
        self.ask = messagebox.askquestion("Ithuba National Lottery", "Do you really want to LOGOUT of the app?")
        if self.ask == 'yes':
            root.destroy()

    def clear(self):
        self.name_entry.delete(0)
        self.email_entry.delete(0)
        self.address_entry.delete(0)
        self.id_entry.delete(0)


if __name__ == '__main__':
    lotto_app = Lotto(root)
    root.mainloop()
