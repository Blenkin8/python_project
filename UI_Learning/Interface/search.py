# search.py
import tkinter as tk
from tkinter import *

from Database.basic import retrieve_data


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topframe = tk.Frame(self, padx=50, pady=50)
        topframe.pack(side="top", fill="both", expand=True)

        searchframe = tk.LabelFrame(topframe, text="Search", padx=10, pady=10)
        searchframe.pack(side="top", fill="both", expand=True)

        txt = tk.Label(
            searchframe,
            text="Name:",
            font=("Arial", 14),
            padx=20,
        )
        txt.grid(row=0, column=0)

        name_entry = tk.Entry(searchframe, width=100)
        name_entry.grid(row=0, column=1, columnspan=3, padx=30)

        retrieve_button = tk.Button(
            searchframe,
            text="Retrieve",
            command=lambda: retrieve_data(name_entry, listbox),
        )
        retrieve_button.grid(row=0, column=5, columnspan=3)

        insert_button = tk.Button(
            searchframe,
            text="Insert",
            command=self.show_insert_page,
            # command=lambda: controller.show_frame(SearchPage)
        )
        insert_button.grid(row=1, column=2, columnspan=3, rowspan=2)

        midframe = tk.Frame(self, padx=50, pady=50)
        midframe.pack(side="top", fill="both", expand=True)

        modeframe = tk.LabelFrame(midframe, text="Searchlist", padx=10, pady=10)
        modeframe.pack(side="top", fill="both", expand=True)

        listbox = tk.Listbox(modeframe, width=100)
        listbox.grid(row=0, column=0, columnspan=5, pady=10)

        delete_button = tk.Button(
            modeframe,
            text="Delete",
            command=lambda: delete_data(name_entry, listbox),
        )
        delete_button.grid(row=0, column=7, rowspan=1, padx=30)

        update_button = tk.Button(
            modeframe,
            text="Update",
            # command=lambda: delete_data(name_entry, listbox),
        )
        update_button.grid(row=1, column=7, rowspan=1, padx=30)

        retrieve_data(name_entry, listbox)

    def show_insert_page(self):
        from Interface.insert import insert

        self.controller.show_frame(insert)

    def retrieve_data(self):
        from Interface.insert import insert

        self.controller.show_frame(insert)
