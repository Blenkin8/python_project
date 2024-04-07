import tkinter as tk

# Must use 'self' often
from Interface.insert import insert
from Interface.search import SearchPage


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (SearchPage, insert):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SearchPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


root = tkinterApp()
root.geometry("960x640")
root.minsize(960, 640)
root.maxsize(960, 640)
root.title("Database Management")
root.mainloop()
