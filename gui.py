
from doctest import master
import tkinter as tk
import tkinter.font as font
import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.introduce()

    # Assigns key "Return" to run subsequent window method.
    # argument func refers to subsequent window method.
    def linkReturn(self, func):
        self.window.bind("<Return>", func)
    # closes current window and opens the next window. also executes ^linkReturn()^.
    def newWindow(self, func):
        if self.window: self.window.destroy()
        self.window = tk.Tk()
        self.FONT = font.Font(size = 20)
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")
        self.linkReturn(func)

    ## WIDGET METHODS ##
    
    def button(self, text, command, padx = 25, pady = 25, bg = "blue", fg = "black"):
        btn = tk.Button(text = text, command = command, padx = padx, pady = pady, bg = bg, fg = fg)
        btn["font"] = self.FONT
        self.pack(btn)
    
    def label(self, text, padx = 25, pady = 25, bg = "blue", fg = "white"):
        self.pack(tk.Label(text = text, padx = padx, pady = pady, bg = bg, fg = fg))
    
    def entry(self, bg = "black", fg = "white"):
        self.pack(self.focus(tk.Entry(bg = bg, fg = fg)))
    
    # Focuses cursor on passed enry widget
    def focus(self, entry):
        entry.focus()
        return entry

    # adds widget to window
    def pack(self, widget, side = "top"):
        widget.pack(side = side)


    ## WINDOW METHODS ##
    
    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newWindow(self.query1)
        self.label("Welcome to Venue Planner!", 0, 50)
        intro = "This application automatically assigns your guests to seats based on information provided."
        self.label(intro, 0, 50)
        self.label("To start enter the name of your venue:", 0, 25)
        self.entry()
        self.button("Submit", self.query1)
        self.window.mainloop()

    # querys for number of tables and max seats per table
    def query1(self, event = None):
        self.newWindow(self.query2)
        self.label("text")
        self.button("Submit", self.query2)
    
    # queries for 
    def query2(self, event = None):
        self.newWindow(self.query3)
    
    # querys for
    def query3(self):
        pass

if __name__ == "__main__":
    bg = bg.Background()
    gui = Gui()
