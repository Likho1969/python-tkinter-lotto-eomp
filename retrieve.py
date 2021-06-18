
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import requests

# setting up window
root = Tk()
# window title
root.title("Ithuba National Lottery Currency Convertor")
root.geometry("1024x768")
render = Image.open("time-currency-s.jpg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Converter:
    def __init__(self):
        # calling API
        self.response = requests.get(" https://v6.exchangerate-api.com/v6/7dba7e6bf61ba339ff735e21/latest/ZAR")
        self.results = self.response.json()

        self.conversion_rates = self.results['conversion_rates']

        self.currency_options = []
        for i in self.conversion_rates.keys():
            self.currency_options.append(i)


    # currency functions
    def convert_currency(self):
        self.num = float(self.amount_entry.get())
        self.ans = self.num * self.results[self.currency_2_cb.get()]
        self.display_amount['text'] = self.ans


    # exit function
    def exit_program(self):
         self.ask = messagebox.askquestion("Ithuba National Lottery- Currency Converter", "Do you really want to exit the app?")
         if self.ask == "yes":
            root.destroy()

    # clear function
    def clear_program(self):
        self.query = messagebox.askquestion("Ithuba National Lottery", "Do you really want to clear the entry(ies)?")
        if self.query == "yes":
            self.amount_entry.delete(0, END)
            self.display_amount.config(text="", bg="#f9db17")
            self.currency_2_cb.delete(0, END)


        # labels
        self.amount = Label(root, text="Your Amount Won:", font="sans-serif 12 bold", bg="#f9db17")
        self.amount.place(x=5, y=180)
        self.currency_1 = Label(root, text="From Currency:", font="sans-serif 12 bold", bg="#f9db17")
        self.currency_1.place(x=5, y=230)
        self.currency_2 = Label(root, text="To Currency:", font="sans-serif 12 bold", bg="#f9db17")
        self.currency_2.place(x=5, y=280)
        self.converted_amount = Label(root, text="Converted Amount:", font="sans-serif 12 bold", bg="#f9db17")
        self.converted_amount.place(x=5, y=330)
        self.display_amount = Label(root, text="", bg="#f9db17")
        self.display_amount.place(x=190, y=330)
        self.currency_value = Label(root, text="Default Currency is set to Rands(ZAR)", bg="#f9db17", font="Consolas 10 bold")
        self.currency_value.place(x=190, y=230)

        # entry
        self.amount_entry = Entry(root)
        self.amount_entry.place(x=190, y=180)

        # combo box
        self.currency_2_cb = Combobox(root)
        self.currency_2_cb['values'] = self.currency_options
        self.currency_2_cb['state'] = 'readonly'
        self.currency_2_cb.set('Select Currency')
        self.currency_2_cb.place(x=190, y=280)
        # currency_2_cb.config(bg="#f9db17")

        # buttons
        clear_btn = Button(root, borderwidth="3", text="Clear", font="sans-serif 15 bold", fg="yellow", bg="blue", command=self.clear_program)
        clear_btn.place(x=5, y=400)
        convert_btn = Button(root, borderwidth="3", text="Convert", font="sans-serif 15 bold", fg="yellow", bg="green", command=self.convert_currency)
        convert_btn.place(x=203, y=400)
        exit_btn = Button(root, borderwidth="3", text="Exit", font="sans-serif 15 bold", fg="black", bg="red", command=self.exit_program)
        exit_btn.place(x=400, y=400)


app = Converter()
# to run the program
root.mainloop()
