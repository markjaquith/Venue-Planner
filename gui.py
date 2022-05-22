
from doctest import master
import tkinter as tk
import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.introduce()

    def getWindow(self):
        return self.window
    # Assigns shorcut key "Return" to function which opens the next window
    def linkReturn(self, func):
        self.window.bind("<Return>", func)
    #closes current window and opens the next window. also, runs function ^above^
    def newWindow(self, func):
        if self.window: self.window.destroy()
        self.window = tk.Tk()
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")
        self.linkReturn(func)

    #made methods for creating widgets so I don't have to type "text =, bg =" etc.
    def button(self, command, padx = 0, pady = 0, bg = "blue", fg = "blue"):
        tk.Button(self.window, command = command, padx = padx, pady = pady, bg = bg, fg = fg)
    
    def label(self, text, padx = 0, pady = 0, bg = "blue", fg = "white"):
        tk.Label(self.window, text = text, padx = padx, pady = pady, bg = bg, fg = fg).pack()
    
    def entry(self, text,  padx = 0, pady = 0, bg = "blue", fg = "white"):
        tk.Entry(self.window, text = text, padx = padx, pady = pady, bg = bg, fg = fg).pack()
    
    ## WINDOW FUNCTIONS ##
    
    # Displays opening message
    def introduce(self):
        self.newWindow(self.query1)
        self.label("Welcome to Venue Planner!", 0, 50)
        self.label("This application automatically assigns your guests to seats based on information provided.", self.window, 0, 50)
        self.label("Press enter or click on the button to begin:", 0, 25)
        self.button(self.query1)
        self.window.mainloop()
    # querys for name of venue
    def query1(self, event = None):
        self.newWindow(self.query2)
        self.label("Please enter the name of your venue:", self.window)
        self.button("continue", self.query2, self.window)
    # querys for number of tables and max seats per table
    def query2(self, event = None):
        self.newWindow(self.query3)
    def query3(self):
        pass
if __name__ == "__main__":
    gui = Gui()
    bg = bg()
