
# importing the required modules
from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image,ImageTk
# creating a window

root = Tk()
root.title("The Winner's Convert")   # naming the recently created window
root.geometry("1170x390")   #  setting the size of the window
root.config(bg="peach puff")   # setting the background color for the window

img = Image.open("Biggest-Currency-Movers.jpg")
render = ImageTk.PhotoImage(img)

img = Label(root, image=render)
img.image = render
img.place(x=0,y=0)

myscrt = StringVar()
myscrt.set("Default Currency is USD$")

r= requests.get("https://v6.exchangerate-api.com/v6/5f5691e2d32d65dbfe9f9300/latest/USD")
print(r.json())

l1 = Label(root,text="Money")
l1.grid(row=2, column=0)

e1 = Entry(root)
e1. grid(row=4, column=0)


btn_active = Button(root, text = "Convert",command=r)
btn_active.grid(row=3, column=2)

l2 = Label(root,text="Current Currency")
l2.grid(row=2, column=5)

e2 = Entry(root,state="readonly",textvariable=myscrt)
e2.grid(row=4, column=5,pady=10)


# defining function that will exit/ close the window/ program
def close():
    close_it = messagebox.askyesno("Notice","Are you sure you want to exit this procedure?")
    if close_it == "Yes":
        root.destroy()

# exit button
exit_btn = Button(text="Exit Program", command=close)
exit_btn.grid(row=9, column=5)

# results shown here
result_entry = Entry(root)
result_entry.grid(row=9, column=2)

# defining function that will delete the figure in the Entry box
def clear():
    e1.delete(0)
    e2.delete(0)
    result_entry.delete(0)


# creating the Clear button and calling the clear()
clear_btn = Button(root, text="Clear", command=clear)
clear_btn.grid(row=9, column=1)


# starting the app
