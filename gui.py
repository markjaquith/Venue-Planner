
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
    
    def button(self, text, command, padx = 25, pady = 25, loc = "top", bg = "blue", fg = "black"):
        btn = tk.Button(text = text, command = command, padx = padx, pady = pady, bg = bg, fg = fg)
        # btn["font"] = self.window.FONT
        self.widgets.append(btn)
        btn.pack()
    
    def label(self, text, padx = 25, pady = 25, loc = "top", bg = "blue", fg = "white", ):
        label = tk.Label(text = text, padx = padx, pady = pady, bg = bg, fg = fg)
        self.widgets.append(label)
        label.pack()

    def entry(self, loc = "top", bg = "black", fg = "white"):
        entry = tk.Entry(bg = bg, fg = fg)
        self.widgets.append(entry)
        entry.pack()
        return entry
    
    # Focuses cursor on passed entry widget argument
    def focus(self, entry):
        entry.focus()

    def columns(self, num):
        for x in range(num):
            self.window.configure(x)

    ## WINDOW METHODS ##
    
    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newForm(self.query1)
        self.label("Welcome to Venue Planner!", 0, 50)
        intro = "This application automatically assigns your guests to seats based on information provided."
        self.label(intro, 0, 50)
        self.label("To start enter the name of your venue:", 0, 25)
        entry = self.entry()
        self.focus(entry)
        self.button("Submit", self.query1)
        self.window.mainloop()

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
