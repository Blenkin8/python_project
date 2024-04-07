import tkinter as tk
from tkinter import messagebox

import mysql.connector as msc
from Interface.search import SearchPage

mydb = msc.connect(host="localhost", user="root", password="mysql", database="test")
mycursor = mydb.cursor()


# Function to retrieve data
def retrieve_data(name_entry, listbox):
    print("name_entry: ", name_entry)
    name = "%" + name_entry.get() + "%"
    if name == "":
        sql = "SELECT * FROM users"
    else:
        sql = "SELECT * FROM users WHERE name LIKE %s"

    mycursor.execute(sql, (name,))
    rows = mycursor.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        # Method 1
        # Convert each element to a string and strip any leading/trailing whitespace
        formatted_row = [str(field).strip() for field in row]
        # Join the formatted elements into a single string with some separator (e.g., comma)
        row_string = ", ".join(formatted_row)
        print(row_string)
        values = row_string.split(", ")
        # Insert the formatted row into the listbox
        listbox.insert(tk.END, values)


# Function to delete data
def delete_data(name_entry, listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        print("Index ", index)
        item = listbox.get(index)
        print("This tuple list: ", item)
        user_id = item[0]
        print(user_id)
        email = item[1]
        print(email)
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)

        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Data deleted successfully.")
        retrieve_data(name_entry, listbox)
    else:
        messagebox.showerror("Error", "No item selected.")


def insert_data(
    name_entry,
    password_entry,
    email_entry,
    amount_entry,
):
    name = name_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    amount = amount_entry.get()

    sql = "INSERT INTO users (name, password, email, amount) VALUES (%s, %s, %s, %s)"
    val = name, password, email, amount  # , age, address

    mycursor.execute(sql, val)
    mydb.commit()

    try:
        messagebox.showinfo("Success", "Data inserted successfully.")
        # controller.show_frame(SearchPage)

    except sql.connector.Error as err:
        if err.errno == msc.ER_WRONG_VALUE:
            # Handle specific error code
            print("Incorrect value provided.")
        else:
            # Handle other database errors
            print("Database error:", err)


# Function to delete data
def update_func(listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        print("Index ", index)
        item = listbox.get(index)
        print("This tuple list: ", item)
        user_id = item[0]
        print(user_id)
        email = item[1]
        print(email)

        # sql = "DELETE FROM users WHERE id = %s"
        # val = (user_id,)

        # mycursor.execute(sql, val)
        # mydb.commit()

    else:
        messagebox.showerror("Error", "No item selected.")


# Function to delete data
def update_data(name_entry, listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        print("Index ", index)
        item = listbox.get(index)
        print(item)
        user_id = item[0]
        print(user_id)
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)

        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Data deleted successfully.")
        retrieve_data(name_entry, listbox)
    else:
        messagebox.showerror("Error", "No item selected.")
