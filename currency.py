
from tkinter import *
import pygame

root = Tk()
root.title("Sound")
root.geometry("500x400")

pygame.mixer.init()


def play():
    pygame.mixer.music.load("button_click_006_53867.mp3")
    pygame.mixer.music.play(loops=0)


my_button = Button(root, text='Play Song', command=play)
my_button.pack(pady=20)

root.mainloop()
