from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk




root = tk.Tk()
root.title("Lotto Draw")
root.geometry("2560x1536")
loader = Image.open("LOTTO BALLS.jpg")
render = ImageTk.PhotoImage(loader)
img = tk.Label(root, image=render)
img.place(x=0, y=0)

lottries = tk.Label(root, text="WALALA WASALA", font=("bold", 20), bg="yellow", fg="black")
lottries.grid(row=1, column=1)

play = tk.Label(root, text="Play!! :", font=("bold", 12), bg="black", fg="white")
play.grid(row=4, column=0)

num1 = tk.IntVar()
num2 = tk.IntVar()
num3 = tk.IntVar()
num4 = tk.IntVar()
num5 = tk.IntVar()
num6 = tk.IntVar()

txt1 = tk.Entry(root, textvariable=num1, font=('bold', 30), width=2)
txt1.grid(row=4, column=2)
txt2 = tk.Entry(root, textvariable=num2, font=('bold', 30), width=2)
txt2.grid(row=4, column=4)
txt3 = tk.Entry(root, textvariable=num3, font=('bold', 30), width=2)
txt3.grid(row=4, column=6)
txt4 = tk.Entry(root, textvariable=num4, font=('bold', 30), width=2)
txt4.grid(row=4, column=8)
txt5 = tk.Entry(root, textvariable=num5, font=('bold', 30), width=2)
txt5.grid(row=4, column=10)
txt6 = tk.Entry(root, textvariable=num6, font=('bold', 30), width=2)
txt6.grid(row=4, column=12)

result_answer = tk.Label(root, width=50, height=8)
result_answer.grid(row=12, column=0)


def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    my_list = [x, y, z, a, b, c]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) < 50:
        messagebox.showinfo("Let's Play", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(text="Jackpot Hurray \n " + "You just got your self Price : R10, 000 000.00 " + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 5:
                result_answer.config(text="Felicitations: " + "You got 5 numbers correct" + "\n With this Outstanding Achievement " + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 4:
                result_answer.config(text="Felicitations: " + "You got 4 numbers correct" + "\n With this Meritorious Achievement " + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 3:
                result_answer.config(text="Felicitations: " + "You got 3 numbers correct" + "\n With this Substantial Achievement " + "You won yourself R100.50 " + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 2:
                result_answer.config(text="Felicitations: " + "You got 2 numbers correct" + "\n With this Adequate Achievement " + "You won yourself R20.00 " + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 1:
                messagebox.showinfo("RESULT", "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
    else:
        messagebox.showinfo("Oops", "Follow the rules")
        num1.delete(0, tk.END)
        num2.delete(0, tk.END)
        num3.delete(0, tk.END)
        num4.delete(0, tk.END)
        num5.delete(0, tk.END)
        num6.delete(0, tk.END)


btn = tk.Button(root, text="PLAY", bg="magenta", command=luck)
btn.grid(row=10, column=0)

root.mainloop()
