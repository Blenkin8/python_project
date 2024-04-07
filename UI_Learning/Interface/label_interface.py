# label_interface.py
from tkinter import *


def create_label(window):
    photo = PhotoImage(file="UI Learning/Images/gears.png")

    label = Label(
        window,
        text="Code Process",
        font=("BlairItcStd", 20, "bold"),
        foreground="green",
        background="black",
        relief=SUNKEN,
        border=10,
        padx=20,
        pady=20,
        image=photo,
        compound="top",
    )
    label.image = photo
    return label
