# Likho Kapesi

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from playsound import playsound


root = tk.Tk()
root.title("ITHUBA National Lottery- iCurrency Converter")
root.geometry("1024x819")
render = Image.open("time-currency-s.jpg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Converter:
    def __init__(self):

        self.results = StringVar()
        self.values1 = StringVar()
        self.values2 = StringVar()

        self.information = requests.get('https://v6.exchangerate-api.com/v6/7dba7e6bf61ba339ff735e21/latest/USD')
        self.information_json = self.information.json()

        self.conversion_rates = self.information_json['conversion_rates']

        self.currency = []
        for i in self.conversion_rates.keys():
            self.currency.append(i)

        self.currency2 = []
        for i in self.conversion_rates.keys():
            self.currency2.append(i)

        self.description_lbl = Label(root, text="1.Rapid currency conversion with ITHUBA National Lottery converter.", bg='yellow', fg="black", font="sans-serif")
        self.description_lbl.place(x=20, y=20)
        self.description_lbl2 = Label(root, text="2.Fast and easy to utilize currency converter. All major currencies included.", bg='yellow', fg="black", font="sans-serif")
        self.description_lbl2.place(x=20, y=40)

        self.currency_option = ttk.Combobox(root)
        self.currency_option['values'] = self.currency
        self.currency_option['state'] = 'readonly'
        self.currency_option.set('Select From-Currency')
        self.currency_option.place(x=200, y=180)

        self.currency_option2 = ttk.Combobox(root)
        self.currency_option2['values'] = self.currency2
        self.currency_option2['state'] = 'readonly'
        self.currency_option2.set('Select To-Currency',)
        self.currency_option2.place(x=500, y=180)

        self.lbl1 = Label(root, text='Enter Amount:', bg='green', fg="yellow", font="sans-serif")
        self.lbl1.place(x=260, y=290)
        self.entry1 = Entry(root, bg='yellow', fg="black", font="sans-serif")
        self.entry1.place(x=400, y=290)
        self.entry1.focus()
        self.lbl2 = Label(root, text='Converted Amount:', bg='green', fg="yellow", font="sans-serif")
        self.lbl2.place(x=230, y=350)
        self.lbl3 = Label(root, text='', textvariable=self.results, bg='yellow', fg="black", font="sans-serif")
        self.lbl3.place(x=410, y=350)


class Currency(Converter):
    def __init__(self):
        super(Currency, self).__init__()
        def convert(currency1, currency2, amount):
            try:
                playsound('click.mp3')
            except:
                 print("Unrecognized audio format")
            if currency1 != 'USD':
                amount = amount / self.conversion_rates[currency1]

            amount = round(amount * self.conversion_rates[currency2], 4)
            return amount

        def calc():
            try:
                amount = float(self.entry1.get())
                currency1 = self.currency_option.get()
                currency2 = self.currency_option2.get()

                amount_converted = convert(currency1, currency2, amount)

                self.results.set(amount_converted)
            except ValueError:
                if self.entry1 != int and self.entry1 != float:
                    try:
                        playsound('beep-05.mp3')
                    except:
                        print("Unrecognized audio format")
                    messagebox.showerror('INVALID', 'You Are Advised to Enter numbers only')

            except requests.exceptions.ConnectionError:
                messagebox.showerror('ERROR', 'Internet Connection is Bad')
            except KeyError:
                messagebox.showerror('ERROR', 'Please Select a Currency')

        # kill program
        def close():
            try:
                playsound('button-4.mp3')
            except:
                print("Unrecognized audio format")
            query = messagebox.askquestion("Closing Application", "Do you want to exit the application?")
            if query == "yes":
                root.destroy()

        def clear():
            try:
                playsound('click.mp3')
            except:
                 print("Unrecognized audio format")
            self.currency_option.set('Select Currency')
            self.currency_option2.set('Select Currency')
            self.entry1.delete(0, END)
            self.entry1.focus()
            self.results.set('')

        self.convert_btn = Button(root, text="CONVERT", borderwidth=3, bg='lime', fg="black", font="sans-serif", command=calc)
        self.convert_btn.place(x=230, y=480)
        self.clear_btn = Button(root, text="CLEAR", borderwidth=3, bg='lime', fg="black", font="sans-serif", command=clear)
        self.clear_btn.place(x=380, y=480)
        self.exit_btn = Button(root, text="EXIT", bg="red", fg="black", borderwidth=3, font="sans-serif", command=close)
        self.exit_btn.place(x=500, y=480)

        self.play_again_button = tk.Button(root, text="Play Again", font="sans-serif 12 bold", bg="lime", fg="black", borderwidth="3", width="15", command=self.play_again)
        self.play_again_button.place(x=280, y=600)

    def play_again(self):
        try:
         playsound('button_click_006_53867.mp3')
        except:
            print("Unrecognized audio format")
        self.question = messagebox.askquestion("ITHUBA National Lottery", "Do you want to TRY ANOTHER LUCK?")
        if self.question == "yes":
            root.destroy()
            import lotto_generator


app = Converter()
app2 = Currency()
root.mainloop()
