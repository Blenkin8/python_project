from tkinter import *


def display(x):
    if x.get() == 1:
        print("Setting Enabled")
    else:
        print("Setting Disabled")


def checkbox(window):
    x = IntVar()

    check_button = Checkbutton(
        window,
        text="Enable setting",
        variable=x,
        onvalue=1,
        offvalue=0,
        command=lambda: display(x),
    )

    check_button.grid(row=2, column=0, padx=10, pady=10)

    return check_button


def radiobutton(window):
    res = ["Low", "Mid", "High"]

    x = IntVar()
    selected_value = StringVar()

    if selected_value == None:
        print("Resolution unavailable")
        selected_value = res[0]
    else:
        print("Resolution Available")
        selected_value.set("Selected value: " + res[x.get()])

    def show_selected_value(selected_value):
        selected_value.set("Selected value: " + res[x.get()])

    for index, option in enumerate(res):
        radiobutton = Radiobutton(
            window,
            text=option,
            variable=x,
            value=index,
            command=lambda: show_selected_value(selected_value),
            indicatoron=0,
        )
        radiobutton.grid(row=2, column=index + 1, padx=10, pady=10, sticky="W")

    selected_label = Label(window, textvariable=selected_value)
    selected_label.grid(row=2, column=4, columnspan=len(res) + 1, rowspan=2)
    print("")

    return radiobutton
