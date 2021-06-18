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


# calling API
response = requests.get(" https://v6.exchangerate-api.com/v6/7dba7e6bf61ba339ff735e21/latest/USD")
results = response.json()

conversion_rates = results['conversion_rates']

currency_options = []
for i in conversion_rates.keys():
    currency_options.append(i)


# currency functions
def convert_currency():
    num = float(amount_entry.get())
    ans = num * results[currency_2_cb.get()]
    display_amount['text'] = ans


# exit function
def exit_program():
    ask = messagebox.askquestion("Ithuba National Lottery- Currency Converter", "Do you really want to exit the app?")
    if ask == "yes":
        root.destroy()

# clear function
def clear_program():
    query = messagebox.askquestion("Ithuba National Lottery", "Do you really want to clear the entry(ies)?")
    if query == "yes":
        amount_entry.delete(0, END)
        display_amount.config(text="", bg="#f9db17")
        currency_2_cb.delete(0, END)


# labels
amount = Label(root, text="Your Amount Won:", font="sans-serif 12 bold", bg="#f9db17")
amount.place(x=5, y=180)
currency_1 = Label(root, text="From Currency:", font="sans-serif 12 bold", bg="#f9db17")
currency_1.place(x=5, y=230)
currency_2 = Label(root, text="To Currency:", font="sans-serif 12 bold", bg="#f9db17")
currency_2.place(x=5, y=280)
converted_amount = Label(root, text="Converted Amount:", font="sans-serif 12 bold", bg="#f9db17")
converted_amount.place(x=5, y=330)
display_amount = Label(root, text="", bg="#f9db17")
display_amount.place(x=190, y=330)
currency_value = Label(root, text="Default Currency is set to Rands(ZAR)", bg="#f9db17", font="Consolas 10 bold")
currency_value.place(x=190, y=230)

# entry
amount_entry = Entry(root)
amount_entry.place(x=190, y=180)

# combo box
currency_2_cb = Combobox(root)
currency_2_cb['values'] = currency_options
currency_2_cb['state'] = 'readonly'
currency_2_cb.set('Select Currency')
currency_2_cb.place(x=190, y=280)
# currency_2_cb.config(bg="#f9db17")

# buttons
clear_btn = Button(root, borderwidth="3", text="Clear", font="sans-serif 15 bold", fg="yellow", bg="blue", command=clear_program)
clear_btn.place(x=5, y=400)
convert_btn = Button(root, borderwidth="3", text="Convert", font="sans-serif 15 bold", fg="yellow", bg="green", command=convert_currency)
convert_btn.place(x=203, y=400)
exit_btn = Button(root, borderwidth="3", text="Exit", font="sans-serif 15 bold", fg="black", bg="red", command=exit_program)
exit_btn.place(x=400, y=400)

# to run the program
root.mainloop()
