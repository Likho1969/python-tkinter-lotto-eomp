from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("SIGN UP")
root.geometry("1000x820")
root.config(background='yellow')
loader = Image.open("phanda.png")
render = ImageTk.PhotoImage(loader)
img = Label(root, image=render)
img.place(x=400, y=130)


# function
def logins():
    log = age_entry.get()
    log1 = int(log)
    if log1 < 18:
        messagebox.showerror("NOTE!!", "Not for person under the age of 18")

    else:
        root.destroy()
        import win
        win.verify()


# labels& entries

head = Label(root, text="YOUR TICKET TO MILLIONNERS", font=("bold", 20), bg="green", fg="white")
head.grid(row=0, column=4)

name = Label(text="NAME", fg="black", bg="yellow", font=("bold", 18))
name.place(x=300, y=323)

nm_entry = Entry(width=24, fg="white", bg="black", font=("bold", 18))
nm_entry.place(x=500, y=320)

sname = Label(text="SURNAME", fg="black", bg="yellow", font=("bold", 18))
sname.place(x=300, y=410)

snm_entry = Entry(width=24, fg="white", bg="black", font=("bold", 18))
snm_entry.place(x=500, y=410)

age = IntVar

age_l = Label(text="AGE", fg="black", bg="yellow", font=("bold", 18))
age_l.place(x=300, y=490)

age_entry = Entry(textvariable=age, width=12, fg="white", bg="black", font=("bold", 18))
age_entry.place(x=500, y=490)

# button

btn = Button(root, text="LOGIN", bg="green", fg="white", command=logins)
btn.place(x=600, y=650)

root.mainloop()
