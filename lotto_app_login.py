# Likho Kapesi

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound

root = tk.Tk()    # create window
root.title("Ithuba National Lottery Login")   # titling window
root.geometry("2560x1536")     # setting window size
root.geometry("2560x1536")
loader = Image.open("powerball-jackpot-2048x1365.jpg")     # background image
render = ImageTk.PhotoImage(loader)
img = Label(root, image=render)
img.place(x=0, y=0)
loader2 = Image.open("ithuba.jpg")
render2 = ImageTk.PhotoImage(loader2)
img2 = tk.Label(root, image=render2)
img2.place(x=300, y=10)


class Lotto:

    """Validating the Login Details"""

    def __init__(self, window):
        # labels& entries

        self.name = tk.Label(window, text="FULL NAME", fg="black", bg="green", font=("sans-serif bold", 18))
        self.name.place(x=300, y=400)

        self.name_entry = tk.Entry(window, width=24, fg="green", bg="yellow", font=("sans-serif bold", 18))
        self.name_entry.place(x=500, y=400)

        self.email_l = tk.Label(window, text="EMAIL ADDRESS", fg="black", bg="green", font=("sans-serif bold", 18))
        self.email_l.place(x=250, y=452)

        self.email_entry = tk.Entry(window, width=24, fg="green", bg="yellow", font=("sans-serif bold", 18))
        self.email_entry.place(x=500, y=450)

        self.address_l = tk.Label(window, text="HOME ADDRESS", fg="black", bg="green", font=("sans-serif bold", 18))
        self.address_l.place(x=250, y=512)

        self.address_entry = tk.Text(window, width=24, fg="green", bg="yellow", height=6, font=("sans-serif bold", 18))
        self.address_entry.place(x=500, y=510)

        self.id_no = IntVar()

        self.id_no_l = tk.Label(window, text="ID NUMBER", width=12, fg="black", bg="green", font=("sans-serif bold", 18))
        self.id_no_l.place(x=250, y=720)

        self.id_entry = tk.Entry(window, textvariable=self.id_no, width=24, fg="green", bg="yellow", font=("sans-serif bold", 18))
        self.id_entry.place(x=500, y=720)

        # button

        self.btn = tk.Button(window, text="LOGIN", bg="green", fg="white", borderwidth="6", font=("sans-serif bold", 18), command=self.id_validation)
        self.btn.place(x=400, y=800)

        self.btn = tk.Button(window, text="LOGOUT", bg="red", fg="white", borderwidth="6", font=("sans-serif bold", 18), command=self.close)
        self.btn.place(x=550, y=800)

        self.btn = tk.Button(window, text="CLEAR", bg="green", fg="white", borderwidth="6", font=("sans-serif bold", 18), command=self.clear)
        self.btn.place(x=720, y=800)

    def id_validation(self):
        try:
         playsound('button_click_006_53867.mp3')
        except:
            print("Unrecognized audio format")
        try:
            self.id_no = int(self.id_entry.get())
            self.id_ls = self.id_entry.get()

            self.year = self.id_entry.get()
            self.year2 = self.id_entry.get()

            self.ithuba_file = open('ithuba_details_file.txt', 'a+')
            self.ithuba_file.write("Player Name: " + self.name_entry.get() + "| Player Email: " + self.email_entry.get() + "| Player ID: " + str(self.id_entry.get()) + "\n",)
            self.ithuba_file.write("\n")
            self.ithuba_file.close()

            if type(self.id_no) == type(str()) or len(self.id_ls) != 13:
                raise ValueError
            elif int(self.year) <= 3:
                messagebox.showinfo(title="Play!", message="Lets Play!")
                root.destroy()
                import lotto_generator
            elif int(self.year2) > 3 and int(self.year2) > 21:
                messagebox.showinfo(title="Grab Your Millions", message="Are You Ready!! Let's dive in and Play!!")
                root.destroy()
                import lotto_generator

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
        try:
         playsound('button-4.mp3')
        except:
            print("Unrecognized audio format")
        self.ask = messagebox.askquestion("Ithuba National Lottery", "Do you really want to LOGOUT of the app?")
        if self.ask == 'yes':
            root.destroy()

    def clear(self):
        try:
         playsound('click.mp3')
        except:
            print("Unrecognized audio format")
        self.query = messagebox.askquestion("ITHUBA National Lottery", "Do you really want to clear the entry(ies)?")
        if self.query == "yes":
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.address_entry.delete(END)
            self.id_entry.delete(0, END)


if __name__ == '__main__':
    lotto_app = Lotto(root)
    root.mainloop()
