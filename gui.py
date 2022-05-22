
from doctest import master
import tkinter as tk
import tkinter.font as font
import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.introduce()

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)
    # closes current window and opens the next window. also executes ^linkReturn()^.


    ## WIDGET METHODS ##
    
    def button(self, text, command, padx = 25, pady = 25, bg = "blue", fg = "black"):
        btn = tk.Button(text = text, command = command, padx = padx, pady = pady, bg = bg, fg = fg)
        btn["font"] = self.FONT
        return btn
    
    def label(self, text, padx = 25, pady = 25, bg = "blue", fg = "white"):
        return tk.Label(text = text, padx = padx, pady = pady, bg = bg, fg = fg)
    
    def entry(self, bg = "black", fg = "white"):
        return self.focus(tk.Entry(bg = bg, fg = fg))
    
    # Focuses cursor on passed enry widget
    def focus(self, entry):
        entry.focus()
        return entry

    # adds widget to window
    def pack(self, widget, side = "top"):
        return widget.pack(side = side)

    def columns(self, num):
        for x in range(num):
            self.window.configure(x)

    ## WINDOW METHODS ##
    
    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newWindow(self.query1)
        self.pack(self.label("Welcome to Venue Planner!", 0, 50))
        intro = "This application automatically assigns your guests to seats based on information provided."
        self.pack(self.label(intro, 0, 50))
        self.pack(self.label("To start enter the name of your venue:", 0, 25))
        self.pack(self.entry())
        self.pack(self.button("Submit", self.query1))
        self.window.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newWindow(self.query2)
        # self.window.grid(0)
        self.pack(self.label("how many seats are there per table?"))
        self.pack(self.label("Please enter an integer:"))
        self.pack(self.entry())
        # self.pack(self.button("Back", self.introduce), "left")
        self.pack(self.button("Submit", self.query2))
        
    # queries for 
    def query2(self, event = None):
        self.newWindow(self.query3)
    
    # querys for
    def query3(self):
        pass

if __name__ == "__main__":
    bg = bg.Background()
    gui = Gui()
