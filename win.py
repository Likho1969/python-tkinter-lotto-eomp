from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Lotto Draw")
root.geometry("2048x1365")
render = Image.open("Daily-Lotto-Results-11-June-2021-2048x1365.jpeg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Play:
    def __init__(self):
        self.lotteries = tk.Label(root, text="WALALA WASALA!! PHANDA PHUSHA PLAY!!", font=("bold", 20), bg="green", fg="black", height=2)
        self.lotteries.place(x=600, y=10)

        self.num1 = tk.IntVar()
        self.num2 = tk.IntVar()
        self.num3 = tk.IntVar()
        self.num4 = tk.IntVar()
        self.num5 = tk.IntVar()
        self.num6 = tk.IntVar()

        self.txt1 = tk.Button(root, textvariable=self.num1, font=('bold', 30), width=2)
        self.txt1.grid(row=4, column=2)
        # creating buttons
        self.btn1 = Button(text="1", command=lambda: self.insert('1, '))
        self.btn1.place(x=10, y=100)
        self.btn2 = Button(text="2", command=lambda: self.insert('2, '))
        self.btn2.place(x=50, y=100)
        self.btn3 = Button(text="3", command=lambda: self.insert('3, '))
        self.btn3.place(x=90, y=100)
        self.btn4 = Button(text="4", command=lambda: self.insert('4, '))
        self.btn4.place(x=130, y=100)
        self.btn5 = Button(text="5", command=lambda: self.insert('5, '))
        self.btn5.place(x=170, y=100)
        self.btn6 = Button(text="6", command=lambda: self.insert('6, '))
        self.btn6.place(x=210, y=100)

        self.btn7 = Button(text="7", command=lambda: self.insert('7, '))
        self.btn7.place(x=10, y=140)
        self.btn8 = Button(text="8", command=lambda: self.insert('8, '))
        self.btn8.place(x=50, y=140)
        self.btn9 = Button(text="9", command=lambda: self.insert('9, '))
        self.btn9.place(x=90, y=140)
        self.btn10 = Button(text="10", width="1", command=lambda: self.insert('10, '))
        self.btn10.place(x=130, y=140,)
        self.btn11 = Button(text="11", width="1", command=lambda: self.insert('11, '))
        self.btn11.place(x=170, y=140,)
        self.btn12 = Button(text="12", width="1", command=lambda: self.insert('12, '))
        self.btn12.place(x=210, y=140)

        self.btn7 = Button(text="13", width="1", command=lambda: self.insert('13, '))
        self.btn7.place(x=10, y=180)
        self.btn8 = Button(text="14", width="1", command=lambda: self.insert('14, '))
        self.btn8.place(x=50, y=180)
        self.btn9 = Button(text="15", width="1", command=lambda: self.insert('15, '))
        self.btn9.place(x=90, y=180,)
        self.btn10 = Button(text="16", width="1", command=lambda: self.insert('16, '))
        self.btn10.place(x=130, y=180,)
        self.btn11 = Button(text="17", width="1", command=lambda: self.insert('17, '))
        self.btn11.place(x=170, y=180,)
        self.btn12 = Button(text="18", width="1", command=lambda: self.insert('18, '))
        self.btn12.place(x=210, y=180)

        self.btn7 = Button(text="19", width="1", command=lambda: self.insert('19, '))
        self.btn7.place(x=10, y=220)
        self.btn8 = Button(text="20", width="1", command=lambda: self.insert('20, '))
        self.btn8.place(x=50, y=220)
        self.btn9 = Button(text="21", width="1", command=lambda: self.insert('21, '))
        self.btn9.place(x=90, y=220,)
        self.btn10 = Button(text="22", width="1", command=lambda: self.insert('22, '))
        self.btn10.place(x=130, y=220,)
        self.btn11 = Button(text="23", width="1", command=lambda: self.insert('23, '))
        self.btn11.place(x=170, y=220,)
        self.btn12 = Button(text="24", width="1", command=lambda: self.insert('24, '))
        self.btn12.place(x=210, y=220)

        self.btn7 = Button(text="25", width="1", command=lambda: self.insert('25, '))
        self.btn7.place(x=10, y=260)
        self.btn8 = Button(text="26", width="1", command=lambda: self.insert('26, '))
        self.btn8.place(x=50, y=260)
        self.btn9 = Button(text="27", width="1", command=lambda: self.insert('27, '))
        self.btn9.place(x=90, y=260,)
        self.btn10 = Button(text="28", width="1", command=lambda: self.insert('28, '))
        self.btn10.place(x=130, y=260,)
        self.btn11 = Button(text="29", width="1", command=lambda: self.insert('29, '))
        self.btn11.place(x=170, y=260,)
        self.btn12 = Button(text="30", width="1", command=lambda: self.insert('30, '))
        self.btn12.place(x=210, y=260)

        self.btn7 = Button(text="31", width="1", command=lambda: self.insert('31, '))
        self.btn7.place(x=10, y=300)
        self.btn8 = Button(text="32", width="1", command=lambda: self.insert('32, '))
        self.btn8.place(x=50, y=300)
        self.btn9 = Button(text="33", width="1", command=lambda: self.insert('33, '))
        self.btn9.place(x=90, y=300,)
        self.btn10 = Button(text="34", width="1", command=lambda: self.insert('34, '))
        self.btn10.place(x=130, y=300,)
        self.btn11 = Button(text="35", width="1", command=lambda: self.insert('35, '))
        self.btn11.place(x=170, y=300,)
        self.btn12 = Button(text="36", width="1", command=lambda: self.insert('36, '))
        self.btn12.place(x=210, y=300)

        self.btn7 = Button(text="37", width="1", command=lambda: self.insert('37, '))
        self.btn7.place(x=10, y=340)
        self.btn8 = Button(text="38", width="1", command=lambda: self.insert('38, '))
        self.btn8.place(x=50, y=340)
        self.btn9 = Button(text="39", width="1", command=lambda: self.insert('39, '))
        self.btn9.place(x=90, y=340,)
        self.btn10 = Button(text="40", width="1", command=lambda: self.insert('40, '))
        self.btn10.place(x=130, y=340,)
        self.btn11 = Button(text="41", width="1", command=lambda: self.insert('41, '))
        self.btn11.place(x=170, y=340,)
        self.btn12 = Button(text="42", width="1", command=lambda: self.insert('42, '))
        self.btn12.place(x=210, y=340)

        self.btn7 = Button(text="43", width="1", command=lambda: self.insert('43, '))
        self.btn7.place(x=10, y=380)
        self.btn8 = Button(text="44", width="1", command=lambda: self.insert('44, '))
        self.btn8.place(x=50, y=380)
        self.btn9 = Button(text="45", width="1", command=lambda: self.insert('45, '))
        self.btn9.place(x=90, y=380,)
        self.btn10 = Button(text="46", width="1", command=lambda: self.insert('46, '))
        self.btn10.place(x=130, y=380,)
        self.btn11 = Button(text="47", width="1", command=lambda: self.insert('47, '))
        self.btn11.place(x=170, y=380,)
        self.btn12 = Button(text="48", width="1", command=lambda: self.insert('48, '))
        self.btn12.place(x=210, y=380)
        self.btn12 = Button(text="49", width="1", command=lambda: self.insert('49, '))
        self.btn12.place(x=10, y=420)

        self.play_btn = Button(text="Play / Play Again", width="12", font="20", borderwidth="6", bg="green", fg="yellow", command=self.luck)
        self.play_btn.place(x=10, y=500)
        self.clear_btn = Button(text="Clear", width="5", font="20", borderwidth="6", command=self.clear)
        self.clear_btn.place(x=190, y=500)
        self.exit_btn = Button(text="Exit", width="5", font="20", bg="red", fg="black", borderwidth="6", command=self.close)
        self.exit_btn.place(x=300, y=500)
        self.claim_btn = Button(text="Claim Prize", width="10", font="20", bg="lime", fg="black", borderwidth="6", command=self.claim)
        self.claim_btn.place(x=10, y=570)

        self.result_answer = tk.Label(root, width=50, height=8, bg="black", fg="yellow")
        self.result_answer.place(x=600, y=700)

        # Number entries

        self.number_label = Label(root, text='Lotto Plus:', bg='yellow', font=('Arial', 35, 'bold'))
        self.number_label.place(x=500, y=200)
        self.number_entry = Entry(root, width=15, font=('Arial', 30, 'bold'), borderwidth=10, state="disabled")
        self.number_entry.place(x=800, y=200)

        self.number_label2 = Label(root, text='Lotto Plus:', bg='yellow', font=('Arial', 30, 'bold'))
        self.number_label2.place(x=500, y=300)
        self.number_entry2 = Entry(root,  width=15, font=('Arial', 30, 'bold'), borderwidth=10, state="disabled")
        self.number_entry2.place(x=800, y=300)

        self.number_label3 = Label(root, text='Lotto:', bg='yellow', font=('Arial', 30, 'bold'))
        self.number_label3.place(x=600, y=400)
        self.number_entry3 = Entry(root,  width=15, font=('Arial', 30, 'bold'), borderwidth=10, state="disabled")
        self.number_entry3.place(x=800, y=400)

        # My Active buttons
        # Lotto Plus Active Button
        self.active_button1 = Button(root, text='ACTIVE', bg='lime', fg='black', font=('Georgia', 10, 'bold'), borderwidth="6", cursor='hand2', command=self.lotto_plus_one)
        self.active_button1.place(x=1200, y=210)
        # Power Ball Active Button
        self.active_button2 = Button(root, text='ACTIVE', bg='lime', fg='black', font=('sans serif', 10, 'bold'), borderwidth="6", cursor='hand2', command=self.lotto_plus_two)
        self.active_button2.place(x=1200, y=310)
        # Lotto Active Button
        self.active_button3 = Button(root, text='ACTIVE', bg='lime', fg='black', font=('sans serif', 10, 'bold'), borderwidth="6", cursor='hand2', command=self.lotto_plus_three)
        self.active_button3.place(x=1200, y=410)

    def luck(self):
        a = self.number_entry.get()
        b = self.number_entry2.get()
        c = self.number_entry3.get()
        d = self.number_entry.get()
        e = self.number_entry2.get()
        f = self.number_entry3.get()

        self.my_list = [a, b, c, d, e, f]
        self.my_list.sort()

        self.todaylotto = sorted(random.sample(range(1, 49), 6))

        if any(self.my_list) < 0 or any(self.my_list) < 50:
                messagebox.showinfo("Let's Play", "Get ready")

                if len(self.todaylotto) == len(self.my_list):
                    same = set(self.todaylotto).intersection(set(self.my_list))
                    if len(same) == 6:
                        self.result_answer.config(text="Jackpot Hurray \n " + "You just got your self Price : R10, 000 000.00 " + "\n Today Lotto Numbers are" + str(self.todaylotto))
                    elif len(same) == 5:
                        self.result_answer.config(text="Felicitations: " + "You got 5 numbers correct" + "\n With this Outstanding Achievement " + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(self.todaylotto))
                    elif len(same) == 4:
                        self.result_answer.config(text="Felicitations: " + "You got 4 numbers correct" + "\n With this Meritorious Achievement " + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(self.todaylotto))
                    elif len(same) == 3:
                        self.result_answer.config(text="Felicitations: " + "You got 3 numbers correct" + "\n With this Substantial Achievement " + "You won yourself R100.50 " + "\n Today Lotto Numbers are" + str(self.todaylotto))
                    elif len(same) == 2:
                        self.result_answer.config(text="Felicitations: " + "You got 2 numbers correct" + "\n With this Adequate Achievement " + "You won yourself R20.00 " + "\n Today Lotto Numbers are" + str(self.todaylotto))
                    elif len(same) == 1:
                        messagebox.showinfo("RESULT", "We are sorry you only got one correct lotto numbers are: " + str(self.todaylotto))
                    elif len(same) == 0:
                        messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(self.todaylotto))
                else:
                    messagebox.showinfo("Oops", "Follow the rules")

    def clear(self):
        self.number_entry.delete(0, tk.END)
        self.number_entry2.delete(0, tk.END)
        self.number_entry3.delete(0, tk.END)

    def close(self):
        self.ask = messagebox.askquestion("Ithuba National Lottery", "Do you really want to exit the app?")
        if self.ask == 'yes':
            root.destroy()

    # Insert Function
    def insert(self, val):
        self.number_entry.insert(END, val)
        self.number_entry2.insert(END, val)
        self.number_entry3.insert(END, val)

    # active entries
    # Lotto Plus
    def lotto_plus_one(self):
        self.number_entry.configure(state='normal')
        self.number_entry2.configure(state='disable')
        self.number_entry3.configure(state='disable')

    # Power Ball
    def lotto_plus_two(self):
        self.number_entry.configure(state='disable')
        self.number_entry2.configure(state='normal')
        self.number_entry3.configure(state='disable')

    # Lotto
    def lotto_plus_three(self):
        self.number_entry.configure(state='disable')
        self.number_entry2.configure(state='disable')
        self.number_entry3.configure(state='normal')

    def claim(self):
        self.query = messagebox.askquestion("You've won!", "Do you want to claim your prize?")
        if self.query == "yes":
            root.destroy()


if __name__ == '__main__':
    app = Play()
    root.mainloop()
