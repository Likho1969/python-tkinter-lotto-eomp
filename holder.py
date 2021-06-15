from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import requests

root = Tk()
root.title("Paypal")
root.geometry("1024x819")
render = Image.open("currency-s.jpg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class Paypal:
        def __init__(self):
            self.convert_btn = tk.Button(root, text="Submit", font=10, borderwidth="10", fg="black")
            self.convert_btn.place(x=5, y=300)
            self.clear_btn = tk.Button(root, text="Clear", borderwidth="10", command=self.clear, fg="black")
            self.clear_btn.place(x=300, y=300)
            self.exit_btn = tk.Button(root, text="Exit", borderwidth="10", command=self.exit_program, fg="black")
            self.exit_btn.place(x=5, y=370)
            self.value = StringVar()
            self.StringVar = IntVar()

            self.information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
            self.information_json = self.information.json()

        def currency(self):
            self.conversion_rate = self.information_json['conversion_rates']
            return self.conversion_rate

            # Creating a label and entries
            self.my_label1 = Label(root, text="Paypal Name", )
            self.my_label1.place(x=5, y=10)

            self.my_entry1 = Entry(root, width=10)
            self.my_entry1.place(x=100, y=10)

            self.my_label2 = Label(root, text="Email address",)
            self.my_label2.place(x=5, y=40)

            self.my_entry2 = Entry(root, width=10)
            self.my_entry2.place(x=100, y=40)

            self.my_label2 = Label(root, text="Choose currency")
            self.my_label2.place(x=5, y=70)


    # Doing the Conversion of the data with its loop
            self.convert_list = Listbox(root, width=20)
            for i in self.conversion_rate.keys():
               self.convert_list.insert(END, str(i))
            self.convert_list.place(x=130, y=90)

        def clear(self):
              self.my_entry1.delete(0, END)


        def exit_program(self):
              root.destroy()
    # creating btn


if __name__ == "__main__":
    my_app = Paypal()
    root.mainloop()
