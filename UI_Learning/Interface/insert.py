# insert.py
import tkinter as tk
from tkinter import *

from Database.basic import *


class insert(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topframe = tk.Frame(self, padx=50, pady=50)
        topframe.pack(side="top", fill="both", expand=True)

        insertframe = tk.LabelFrame(
            topframe,
            text="Enter the data",
        )
        insertframe.pack(side="top", fill="both", expand=True)

        txt = tk.Label(
            insertframe,
            text="Name:",
            font=("Arial", 14),
            padx=20,
        )
        txt.grid(row=0, column=0)

        name_entry = tk.Entry(insertframe, width=50)
        name_entry.grid(row=0, column=1, columnspan=3, padx=30)

        password = tk.Label(
            insertframe,
            text="Password:",
            font=("Arial", 14),
            padx=20,
        )
        password.grid(row=1, column=0)

        password_entry = tk.Entry(insertframe, width=50)
        password_entry.grid(row=1, column=1, columnspan=3, padx=30)

        email = tk.Label(
            insertframe,
            text="Email:",
            font=("Arial", 14),
            padx=20,
        )
        email.grid(row=2, column=0)

        email_entry = tk.Entry(insertframe, width=50)
        email_entry.grid(row=2, column=1, columnspan=3, padx=30)

        amount = tk.Label(
            insertframe,
            text="Amount:",
            font=("Arial", 14),
            padx=20,
        )
        amount.grid(row=3, column=0)

        amount_entry = tk.Entry(insertframe, width=50)
        amount_entry.grid(row=3, column=1, columnspan=3, padx=30)

        # Buttons
        btn_back = tk.Button(
            topframe,
            text="Back",
            command=self.show_search_page,
            # lambda: controller.show_frame(SearchPage)
        )
        btn_back.pack(side="left")

        btn_submit = tk.Button(
            topframe,
            text="Submit",
            command=lambda: insert_data(
                name_entry,
                password_entry,
                email_entry,
                amount_entry,
            ),
            # command=self.show_search_page,
        )
        btn_submit.pack(side="right")

    def show_search_page(self):
        from Interface.search import SearchPage

        self.controller.show_frame(SearchPage)
