# button_interface.py
from tkinter import *

count = 0


def click():
    global count
    count += 1
    print("Clicked", count)


def comicsans(size):
    return (("Comic Sans", size),)


def testbtn(window):
    photo = PhotoImage(file="UI Learning/Images/confirm.png")
    button = Button(
        window,
        text="Click",
        height=80,
        width=100,
        command=click,
        font=comicsans(30),
        foreground="#00FF00",
        background="black",
        activeforeground="#00FF00",
        activebackground="black",
        state=ACTIVE,
        image=photo,
        compound="bottom",
    )
    button.image = photo

    return button
