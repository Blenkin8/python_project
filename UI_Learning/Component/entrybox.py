from tkinter import *


def submit(entry):
    username = entry.get()
    print("Hello " + username)


def delete(entry):
    entry.delete(0, END)


def backspace(entry):
    entry.delete(len(entry.get()) - 1, END)


def testentry(window):
    entry = Entry(window, font=("Arial", 12), show="*")
    entry.grid(row=1, column=0, padx=10, pady=10)

    submit_button = Button(window, text="submit", command=lambda: submit(entry))
    submit_button.grid(row=1, column=1, padx=10, pady=10)

    submit_button = Button(window, text="delete", command=lambda: delete(entry))
    submit_button.grid(row=1, column=2, padx=10, pady=10)

    submit_button = Button(window, text="backspace", command=lambda: backspace(entry))
    submit_button.grid(row=1, column=3, padx=10, pady=10)

    return entry, submit_button
