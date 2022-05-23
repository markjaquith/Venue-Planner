
import tkinter as tk
import tkinter.font as font
import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.widgets = list()
        self.introduce()

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)
    # closes current window and opens the next window. also executes ^linkReturn()^.
    def newForm(self, func):
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        # self.window.FONT = font.Font(size = 20)
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")
        self.linkReturn(func)

    ## WIDGET METHODS ##

    def button(self, **kwargs):
        btn = tk.Button(kwargs, padx = 25, pady = 25, bg = "blue", fg = "white")
        # btn["font"] = self.window.FONT
        self.widgets.append(btn)

    def label(self, **kwargs):
        label = tk.Label(kwargs)
        # , padx = 0, pady = 25, bg = "blue", fg = "white")
        self.widgets.append(label)

    def entry(self, **kwargs):
        entry = tk.Entry(kwargs)
        self.widgets.append(entry)
    
    # Focuses cursor on passed entry widget argument
    def focus(self, entry):
        entry.focus()

    def columns(self, num):
        for x in range(num):
            self.window.configure(x)
    
    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newForm(self.query1)
        text = "This application automatically assigns your guests to seats based on information provided."
        self.label(text = text).pack()
        text = "To start enter the name of your venue:"
        self.label(text = text),pack()
        entry = self.entry().pack(side = RIGHT)
        self.focus(entry)
        self.button("Submit", self.query1).pack()
        tk.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newForm(self.query2)
        # self.window.grid(0)
        self.label("how many seats are there per table?")
        self.label("Please enter an integer:")
        tk.Entry().pack()
        self.button("Submit", self.query2)
        
    # queries for 
    def query2(self, event = None):
        self.newForm(self.query3)
    
    # querys for
    def query3(self):
        pass

if __name__ == "__main__":
    bg = bg.Background()
    gui = Gui()
