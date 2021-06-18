
from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from random import sample


root = tk.Tk()
root.title("Lotto Draw / Generator - Ithuba National Lottery")
root.geometry("2048x1365")
render = Image.open("Daily-Lotto-Results-11-June-2021-2048x1365.jpeg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Play:
    def __init__(self):
        self.lotteries = tk.Label(root, text="WALALA WASALA!! PHANDA PHUSHA PLAY!!", font=("bold", 20), bg="green", fg="black", height=2)
        self.lotteries.place(x=600, y=10)

        # label and entry for user numbers
        self.user_num_lbl = Label(root, text='Set 1:', bg="green", font="sans-serif 12 bold")  # set1
        self.user_num_lbl.place(x=270, y=300)
        self.user_num_entry = Entry(root, width=5, bg="yellow")
        self.user_num_entry.place(x=340, y=300)
        self.user_num_lbl2 = Label(root, text='Set 2:', bg="green", font="sans-serif 12 bold")  # set2
        self.user_num_lbl2.place(x=270, y=330)
        self.user_num_entry2 = Entry(root, width=5, bg="yellow")
        self.user_num_entry2.place(x=340, y=330)
        self.user_num_lbl3 = Label(root, text='Set 3:', bg="green", font="sans-serif 12 bold")  # set3
        self.user_num_lbl3.place(x=270, y=360)
        self.user_num_entry3 = Entry(root, width=5, bg="yellow")
        self.user_num_entry3.place(x=370, y=300)
        self.user_num_entry4 = Entry(root, width=5, bg="yellow")
        self.user_num_entry4.place(x=400, y=300)
        self.user_num_entry5 = Entry(root, width=5, bg="yellow")
        self.user_num_entry5.place(x=430, y=300)
        self.user_num_entry6 = Entry(root, width=5, bg="yellow")
        self.user_num_entry6.place(x=460, y=300)
        self.user_num_entry7 = Entry(root, width=5, bg="yellow")
        self.user_num_entry7.place(x=490, y=300)
        self.user_num_entry8 = Entry(root, width=5, bg="yellow")
        self.user_num_entry8.place(x=370, y=330)
        self.user_num_entry9 = Entry(root, width=5, bg="yellow")
        self.user_num_entry9.place(x=400, y=330)
        self.user_num_entry10 = Entry(root, width=5, bg="yellow")
        self.user_num_entry10.place(x=430, y=330)
        self.user_num_entry11 = Entry(root, width=5, bg="yellow")
        self.user_num_entry11.place(x=460, y=330)
        self.user_num_entry12 = Entry(root, width=5, bg="yellow")
        self.user_num_entry12.place(x=490, y=330)
        self.user_num_entry13 = Entry(root, width=5, bg="yellow")
        self.user_num_entry13.place(x=340, y=360)
        self.user_num_entry14 = Entry(root, width=5, bg="yellow")
        self.user_num_entry14.place(x=370, y=360)
        self.user_num_entry15 = Entry(root, width=5, bg="yellow")
        self.user_num_entry15.place(x=400, y=360)
        self.user_num_entry16 = Entry(root, width=5, bg="yellow")
        self.user_num_entry16.place(x=430, y=360)
        self.user_num_entry17 = Entry(root, width=5, bg="yellow")
        self.user_num_entry17.place(x=460, y=360)
        self.user_num_entry18 = Entry(root, width=5, bg="yellow")
        self.user_num_entry18.place(x=490, y=360)

        # instructions
        self.user_instructions = Label(root, text='Instructions:', bg="green", font="sans-serif 12 bold")
        self.user_instructions.place(x=5, y=180)
        self.user_instructions1 = Label(root, text='1. You have up to 3 sets to enter 6 different numbers', bg="lime", font="sans-serif 12 bold", fg="black")
        self.user_instructions1.place(x=5, y=200)
        self.user_instructions2 = Label(root, text='2. You have to choose 6 different numbers ranging from 1-49', bg="lime", font="sans-serif 12 bold", fg="black")
        self.user_instructions2.place(x=5, y=220)
        self.user_instructions3 = Label(root, text='3. Click Check Numbers to view the winning Lotto Numbers', bg="lime", font="sans-serif 12 bold", fg="black")
        self.user_instructions3.place(x=5, y=242)

        self.app_disclaimer = Label(root, text='Disclaimer:', bg="red2", font="sans-serif 12 bold")
        self.app_disclaimer.place(x=700, y=180)
        self.user_instructions1 = Label(root, text='Although ITHUBA takes every care to ensure the accuracy of information containing the National Lottery results, ITHUBA', bg="orangered", font="sans-serif 12 bold", fg="black")
        self.user_instructions1.place(x=700, y=200)
        self.user_instructions2 = Label(root, text='cannot take any responsibility  for any errors, mistakes or omissions contained herein. ', bg="orangered", font="sans-serif 12 bold", fg="black")
        self.user_instructions2.place(x=700, y=220)
        self.user_instructions3 = Label(root, text="The National Lottery results contained in the official records maintained by ITHUBA's ", bg="orangered", font="sans-serif 12 bold", fg="black")
        self.user_instructions3.place(x=700, y=242)
        self.user_instructions4 = Label(root, text="Central Lottery system will prevail and all games Rules and Regulations shall be applicable.", bg="orangered", font="sans-serif 12 bold", fg="black")
        self.user_instructions4.place(x=700, y=262)

        # button
        self.lotto_btn = Button(root, text="Play / Play Again", bg="lime", font="sans-serif 12 bold", borderwidth="3", fg="black", highlightthickness=0, command=self.generate_nums)
        self.lotto_btn.place(x=10, y=550)
        self.clear_btn = Button(root, text='Clear', command=self.clear_input, bg="green", font="sans-serif 12 bold", borderwidth="3", fg="black", highlightthickness=0)
        self.clear_btn.place(x=200, y=550)
        self.exit_btn = Button(root, text='Exit', command=self.close, bg="red", font="sans-serif 12 bold", borderwidth="3", fg="black", highlightthickness=0)
        self.exit_btn.place(x=300, y=550)

        self.claim_btn = Button(root, text="Claim Prize", bg="lime", font="sans-serif 12 bold", fg="black", borderwidth="3", command=self.banking_details)
        self.claim_btn.place(x=10, y=620)

        self.currency_btn = Button(root, text="Currency Convertor", bg="blue", font="sans-serif 12 bold", fg="black", command=self.currency_convertor, borderwidth=3)
        self.currency_btn.place(x=170, y=620)

        # display numbers header label
        self.lotto_num_header = Label(root, text='The Lotto Numbers Are:', bg='green', fg='yellow', font="sans-serif 12 bold")
        self.lotto_num_header.place(x=300, y=400)

        # display numbers label
        self.lotto_num_lbl1 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl1.place(x=310, y=450)
        self.lotto_num_lbl2 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl2.place(x=340, y=450)
        self.lotto_num_lbl3 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl3.place(x=370, y=450)
        self.lotto_num_lbl4 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl4.place(x=400, y=450)
        self.lotto_num_lbl5 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl5.place(x=430, y=450)
        self.lotto_num_lbl6 = Label(root, width=4, height=2, bg="lime", text='')
        self.lotto_num_lbl6.place(x=460, y=450)

    winnings = ["R0", "R20", "R100.50", "R2,384", "R8,584", "R10,000,000"]
    lotto_list1 = []
    lotto_list2 = []
    lotto_list3 = []

    def generate_list1(self):
        self.lotto_list1.append(self.user_num_entry.get())
        self.lotto_list1.append(self.user_num_entry4.get())
        self.lotto_list1.append(self.user_num_entry5.get())
        self.lotto_list1.append(self.user_num_entry6.get())
        self.lotto_list1.append(self.user_num_entry7.get())
        self.lotto_list1.append(self.user_num_entry8.get())

    def generate_list2(self):
        num7 = self.user_num_entry2.get()
        num8 = self.user_num_entry8.get()
        num9 = self.user_num_entry9.get()
        num10 = self.user_num_entry10.get()
        num11 = self.user_num_entry11.get()
        num12 = self.user_num_entry12.get()
        list_2 = num7, num8, num9, num10, num11, num12
        return list_2

    def generate_list3(self):
        num13 = self.user_num_entry3.get()
        num14 = self.user_num_entry14.get()
        num15 = self.user_num_entry15.get()
        num16 = self.user_num_entry16.get()
        num17 = self.user_num_entry17.get()
        num18 = self.user_num_entry18.get()
        list_3 = num13, num14, num15, num16, num17, num18
        return list_3

    def generate_nums(self):
        self.lotto_list1.append(int(self.user_num_entry.get()))
        self.lotto_list1.append(int(self.user_num_entry3.get()))
        self.lotto_list1.append(int(self.user_num_entry4.get()))
        self.lotto_list1.append(int(self.user_num_entry5.get()))
        self.lotto_list1.append(int(self.user_num_entry6.get()))
        self.lotto_list1.append(int(self.user_num_entry7.get()))
        self.lotto_nums = random.sample(range(1, 49), 6)
        self.lotto_nums.sort()
        self.lotto_num_lbl1.configure(text=self.lotto_nums[0], bg="white")
        self.lotto_num_lbl2.configure(text=self.lotto_nums[1], bg="white")
        self.lotto_num_lbl3.configure(text=self.lotto_nums[2], bg="white")
        self.lotto_num_lbl4.configure(text=self.lotto_nums[3], bg="white")
        self.lotto_num_lbl5.configure(text=self.lotto_nums[4], bg="white")
        self.lotto_num_lbl6.configure(text=self.lotto_nums[5], bg="white")

        self.lotto = 0
        for x in self.lotto_nums:
            if x in self.lotto_list1:
                self.lotto += 1
        if self.lotto <= 1:
            messagebox.showinfo("Bad Luck!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[0])
        elif self.lotto == 2:
            messagebox.showinfo("Congratulations!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[1])
        elif self.lotto == 3:
            messagebox.showinfo("Congratulations!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[2])
        elif self.lotto == 4:
            messagebox.showinfo("Congratulations!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[3])
        elif self.lotto == 5:
            messagebox.showinfo("Congratulations!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[4])
        elif self.lotto == 6:
            messagebox.showinfo("Congratulations!", str(self.lotto) + " " + "Numbers" + "\n" + "Your Winnings Are:" + self.winnings[5])
        return self.lotto_nums

    def banking_details(self):
        self.question = messagebox.askquestion("Ithuba National Lottery", "Do you wish to claim your winnings?")
        if self.question == "yes":
            messagebox.showinfo("Disclaimer", "Please Enter Your Bank Details In The Next Window")
            root.destroy()
            import Bank

    def currency_convertor(self):
        self.ask = messagebox.askquestion("Ithuba National Lottery", "Do you wish to convert your winnings?")
        if self.ask == "yes":
            messagebox.showinfo("Successful", "Hi Player, welcome to Ithuba National Lottery Currency Converter")
            root.destroy()
            import currency

    def clear_input(self):
        self.enquiry = messagebox.askquestion("Ithuba National Lottery - Lotto Generator", "Do you really want to clear the entry(ies)?")
        if self.enquiry == "yes":
            self.user_num_entry.delete(0, END)
            self.user_num_entry2.delete(0, END)
            self.user_num_entry3.delete(0, END)
            self.user_num_entry4.delete(0, END)
            self.user_num_entry5.delete(0, END)
            self.user_num_entry6.delete(0, END)
            self.user_num_entry7.delete(0, END)
            self.user_num_entry8.delete(0, END)
            self.user_num_entry9.delete(0, END)
            self.user_num_entry10.delete(0, END)
            self.user_num_entry11.delete(0, END)
            self.user_num_entry12.delete(0, END)
            self.user_num_entry13.delete(0, END)
            self.user_num_entry14.delete(0, END)
            self.user_num_entry15.delete(0, END)
            self.user_num_entry16.delete(0, END)
            self.user_num_entry17.delete(0, END)
            self.user_num_entry18.delete(0, END)
            self.lotto_num_lbl1.config(text='', bg="lime")
            self.lotto_num_lbl2.config(text='', bg="lime")
            self.lotto_num_lbl3.config(text='', bg="lime")
            self.lotto_num_lbl4.config(text='', bg="lime")
            self.lotto_num_lbl5.config(text='', bg="lime")
            self.lotto_num_lbl6.config(text='', bg="lime")

    def close(self):
        self.query = messagebox.askquestion("Ithuba National Lottery - Lotto Generator", "Do you really want to close the app?")
        if self.query == "yes":
            root.destroy()


app = Play()
root.mainloop()
