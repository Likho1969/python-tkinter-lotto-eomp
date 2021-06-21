
from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image,ImageTk


root = Tk()
root.title("ITHUBA National Lottery Currency Converter")
root.geometry("1024x819")

img = Image.open("time-currency-s.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)

abc = StringVar()
abc.set("Default Currency is USD$")

req = requests.get(" https://v6.exchangerate-api.com/v6/7dba7e6bf61ba339ff735e21/latest/USD")
print(req.json())

l1 = Label(root, text="Winnings", font="sans-serif 12 bold", bg="green", fg="yellow")
l1.place(x=100, y=300)

entry1 = Entry(root)
entry1.place(x=200, y=300)


btn_active = Button(root, text="Convert", font="sans-serif 12 bold", bg="green", fg="yellow", command=req)
btn_active.grid(row=3, column=2)

l2 = Label(root, text="Current Currency", font="sans-serif 12 bold", bg="green", fg="yellow")
l2.grid(row=2, column=5)

entry2 = Entry(root, state="readonly", textvariable=abc)
entry2.grid(row=4, column=5, pady=10)


# defining function that will exit/ close the window/ program
def close():
    query = messagebox.askquestion("ITHUBA National Lottery", "Are you sure you want to exit this procedure?")
    if query == "yes":
        root.destroy()


# exit button
exit_btn = Button(text="Exit Program", command=close)
exit_btn.grid(row=9, column=5)

# results shown here
result_entry = Entry(root)
result_entry.grid(row=9, column=2)


# defining function that will delete the figure in the Entry box
def clear():
    entry1.delete(0)
    entry2.delete(0)
    result_entry.delete(0)


# creating the Clear button and calling the clear()
clear_btn = Button(root, text="Clear", command=clear)
clear_btn.grid(row=9, column=1)


# starting the app
root.mainloop()
