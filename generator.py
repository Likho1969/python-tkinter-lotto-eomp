
from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk


def verify():
    pass


root = tk.Tk()
root.title("Lotto Generator")
root.geometry("2048x1365")
render = Image.open("Daily-Lotto-Results-11-June-2021-2048x1365.jpeg")
loader = ImageTk.PhotoImage(render)
img = tk.Label(root, image=loader)
img.place(x=0, y=0)


class LottoGenerator:
    def __init__(self):
            self.head_label = tk.Label(text="Panda, Pusha , Play.", bg="green")
            self.head_label.place(x=270, y=10)

            self.output = Label(text="", width="30", height="2")
            self.output.place(x=380, y=140)
            self.output = Label(text="", width="30", height="2")
            self.output.place(x=380, y=185)
            self.output = Label(text="", width="30", height="2")
            self.output.place(x=380, y=230)
            self.number_label = Label(root, text="Your numbers")
            self.number_label.place(x=380, y=100)

            # creating buttons
            self.btn1 = Button(text="1")
            self.btn1.place(x=10, y=100)
            self.btn2 = Button(text="2")
            self.btn2.place(x=50, y=100)
            self.btn3 = Button(text="3")
            self.btn3.place(x=90, y=100)
            self.btn4 = Button(text="4")
            self.btn4.place(x=130, y=100)
            self.btn5 = Button(text="5")
            self.btn5.place(x=170, y=100)
            self.btn6 = Button(text="6")
            self.btn6.place(x=210, y=100)

            self.btn7 = Button(text="7")
            self.btn7.place(x=10, y=140)
            self.btn8 = Button(text="8")
            self.btn8.place(x=50, y=140)
            self.btn9 = Button(text="9")
            self.btn9.place(x=90, y=140)
            self.btn10 = Button(text="10", width="1")
            self.btn10.place(x=130, y=140,)
            self.btn11 = Button(text="11", width="1")
            self.btn11.place(x=170, y=140,)
            self.btn12 = Button(text="12", width="1")
            self.btn12.place(x=210, y=140)

            self.btn7 = Button(text="13", width="1")
            self.btn7.place(x=10, y=180)
            self.btn8 = Button(text="14", width="1")
            self.btn8.place(x=50, y=180)
            self.btn9 = Button(text="15", width="1")
            self.btn9.place(x=90, y=180,)
            self.btn10 = Button(text="16", width="1")
            self.btn10.place(x=130, y=180,)
            self.btn11 = Button(text="17", width="1")
            self.btn11.place(x=170, y=180,)
            self.btn12 = Button(text="18", width="1")
            self.btn12.place(x=210, y=180)

            self.btn7 = Button(text="19", width="1")
            self.btn7.place(x=10, y=220)
            self.btn8 = Button(text="20", width="1")
            self.btn8.place(x=50, y=220)
            self.btn9 = Button(text="21", width="1")
            self.btn9.place(x=90, y=220,)
            self.btn10 = Button(text="22", width="1")
            self.btn10.place(x=130, y=220,)
            self.btn11 = Button(text="23", width="1")
            self.btn11.place(x=170, y=220,)
            self.btn12 = Button(text="24", width="1")
            self.btn12.place(x=210, y=220)

            self.btn7 = Button(text="25", width="1")
            self.btn7.place(x=10, y=260)
            self.btn8 = Button(text="26", width="1")
            self.btn8.place(x=50, y=260)
            self.btn9 = Button(text="27", width="1")
            self.btn9.place(x=90, y=260,)
            self.btn10 = Button(text="28", width="1")
            self.btn10.place(x=130, y=260,)
            self.btn11 = Button(text="29", width="1")
            self.btn11.place(x=170, y=260,)
            self.btn12 = Button(text="30", width="1")
            self.btn12.place(x=210, y=260)

            self.btn7 = Button(text="31", width="1")
            self.btn7.place(x=10, y=300)
            self.btn8 = Button(text="32", width="1")
            self.btn8.place(x=50, y=300)
            self.btn9 = Button(text="33", width="1")
            self.btn9.place(x=90, y=300,)
            self.btn10 = Button(text="34", width="1")
            self.btn10.place(x=130, y=300,)
            self.btn11 = Button(text="35", width="1")
            self.btn11.place(x=170, y=300,)
            self.btn12 = Button(text="36", width="1")
            self.btn12.place(x=210, y=300)

            self.btn7 = Button(text="37", width="1")
            self.btn7.place(x=10, y=340)
            self.btn8 = Button(text="38", width="1")
            self.btn8.place(x=50, y=340)
            self.btn9 = Button(text="39", width="1")
            self.btn9.place(x=90, y=340,)
            self.btn10 = Button(text="40", width="1")
            self.btn10.place(x=130, y=340,)
            self.btn11 = Button(text="41", width="1")
            self.btn11.place(x=170, y=340,)
            self.btn12 = Button(text="42", width="1")
            self.btn12.place(x=210, y=340)

            self.btn7 = Button(text="43", width="1")
            self.btn7.place(x=10, y=380)
            self.btn8 = Button(text="44", width="1")
            self.btn8.place(x=50, y=380)
            self.btn9 = Button(text="45", width="1")
            self.btn9.place(x=90, y=380,)
            self.btn10 = Button(text="46", width="1")
            self.btn10.place(x=130, y=380,)
            self.btn11 = Button(text="47", width="1")
            self.btn11.place(x=170, y=380,)
            self.btn12 = Button(text="48", width="1")
            self.btn12.place(x=210, y=380)
            self.btn12 = Button(text="49", width="1")
            self.btn12.place(x=10, y=420)

            self.btn12 = Button(text="Play", width="5", font="20")
            self.btn12.place(x=10, y=500)
            self.btn12 = Button(text="Clear", width="5", font="20")
            self.btn12.place(x=100, y=500)
            self.btn12 = Button(text="Exit", width="5", borderwidth=6, font="20")
            self.btn12.place(x=200, y=500)


if __name__ == '__main__':
    lotto_app = LottoGenerator()
    root.mainloop()
