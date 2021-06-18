
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox

# setting up the window
root = Tk()
root.title("Banking Details")  # window title
root.config(bg="#f9db17")
root.geometry("1024x768")
render = Image.open("Bank.jpg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Bank:
    def __init__(self):
        # account labels
        self.account_nm = Label(root, text="Account Holder:", font="sans-serif 12 bold", bg="green", fg="yellow")
        self.account_nm.place(x=300, y=180)
        self.account_fig = Label(root, text="Account Number:", font="sans-serif 12 bold", bg="green", fg="yellow")
        self.account_fig.place(x=300, y=230)
        self.branch_fig = Label(root, text="Branch Code:", font="sans-serif 12 bold", bg="green", fg="yellow")
        self.branch_fig.place(x=300, y=280)
        self.type_of_bank = Label(root, text="Choose Your Bank:", font="sans-serif 12 bold", bg="green", fg="yellow")
        self.type_of_bank.place(x=300, y=330)

        # account entries
        self.account_nm_entry = Entry(root, bg="yellow", fg="black")
        self.account_nm_entry.place(x=500, y=180)
        self.account_fig_entry = Entry(root, bg="yellow", fg="black")
        self.account_fig_entry.place(x=500, y=230)
        self.branch_fig_entry = Entry(root, bg="yellow", fg="black")
        self.branch_fig_entry.place(x=500, y=280)

        # ComboBox
        self.bank_combobox = Combobox(root)
        self.bank_combobox["values"] = "Capitec Bank", "FNB", "Standard Bank", "Absa Bank", "Nedbank", "Discovery Bank", "African Bank", "Investec"
        self.bank_combobox.place(x=500, y=330)
        self.bank_combobox.set("Choose Your Bank")
        self.bank_combobox['state'] = 'readonly'

        self.exit_button = Button(root, text="Exit", font="sans-serif 12 bold", bg="red", fg="yellow", borderwidth="3", command=self.exit_program)
        self.exit_button.place(x=600, y=500)

        self.clear_button = Button(root, text="Clear", font="sans-serif 12 bold", bg="lime", fg="black", borderwidth="3", command=self.clear_input)
        self.clear_button.place(x=500, y=500)

        # buttons
        self.submit_button = Button(root, text="Submit Your Claim", font="sans-serif 12 bold", bg="lime", fg="black", borderwidth="3", width="15", command=self.bank_number)
        self.submit_button.place(x=280, y=500)

        # exit function
    def exit_program(self):
        query = messagebox.askquestion("Ithuba National Lottery", "Are you sure you want to exit the app")
        if query == "yes":
            return root.destroy()

    # clear function
    def clear_input(self):
        ask = messagebox.askquestion("Clear Entries", "Do you want to clear the entries?")
        if ask == "yes":
            self.account_nm_entry.delete(0, END)
            self.account_fig_entry.delete(0, END)
            self.branch_fig_entry.delete(0, END)

    # bank function
    def bank_number(self):
         try:
            bank_num = self.account_fig_entry.get()
            branch = self.branch_fig_entry.get()
            if len(bank_num) == 11 and len(branch) == 6:
                 self.f = open("ithuba_details_file.txt", "a+")
                 self.f.write(
                       self.account_fig_entry.get() + " " + self.account_fig_entry.get() + " " + self.branch_fig_entry.get() + " " + self.bank_combobox.get() + "\n")
                 self.f.close()
                 messagebox.showinfo("Successful", "Please Check Your Email For Further Instructions")
            else:
                messagebox.showinfo("Failed", "You are Kindly Advised to Please Enter A 11 Digit Bank Account Number and A 6 Digit Branch Code")
         except ValueError(str):
            messagebox.showinfo("Invalid", "You are kindly Advised to Please Utilize Digits Only")


app = Bank()
# to run the program
root.mainloop()
