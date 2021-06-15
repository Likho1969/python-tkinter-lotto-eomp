
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300")
root.title("Payment Methods")


class Method:
    def _init_(self):
        self.head_label = Label(root, text="Choose Payment Method")
        self.head_label.place(x=170, y=10)

        self.category_lbl = Label(root, text="Select Payment Method:")
        self.category_lbl.place(x=10, y=80)
        self.var = StringVar()
        self.category_list = ttk.Combobox(root, textvariable=self.var, width=12, value=["Bank Acc", "Paypal"])
        self.category_list.place(x=200, y=80)

        self.btn1 = Button(root, text="Next")
        self.btn1.place(x=10, y=120)


app = Method()
root.mainloop()
