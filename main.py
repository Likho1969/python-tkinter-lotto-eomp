from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("SIGN UP")
root.geometry("1000x820")
root.config(background='yellow')
loader = Image.open("nation.webp")
render = ImageTk.PhotoImage(loader)
img = Label(root, image=render)
img.place(x=0, y=0)


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

name = Label(text="NAME", fg="black", font=("bold", 18))
name.grid(row=2, column=0)

nm_entry = Entry(width=24, fg="black", font=("bold", 18))
nm_entry.grid(row=2, column=6)

sname = Label(text="SURNAME", fg="black", font=("bold", 18))
sname.grid(row=4, column=0)

snm_entry = Entry(width=24, fg="black", font=("bold", 18))
snm_entry.grid(row=4, column=6)

age = IntVar

age_l = Label(text="AGE", fg="black", font=("bold", 18))
age_l.grid(row=6, column=0)

age_entry = Entry(textvariable=age, width=12, fg="black", font=("bold", 18))
age_entry.grid(row=6, column=6)

# button

btn = Button(root, text="LOGIN", bg="magenta", command=logins)
btn.grid(row=8, column=4)

root.mainloop()
