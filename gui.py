
import tkinter as tk
# import tkinter.font as font'

import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.widgets = list()
        self.introduce()

    # closes current window and opens the next window.
    def newWindow(self):
        self.window.destroy()    
        self.window = tk.Tk()
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")     

    ## WIDGET METHODS ##
    ## each method creates a widget.

    def label(self, *args, **kwargs):
        label = tk.Label(*args, **kwargs, bg = "blue", fg = "white")
        return label

    def entry(self, *args, **kwargs):
        entry = tk.Entry(*args, **kwargs)
        return entry

    def button(self, *args, **kwargs):
        btn = tk.Button(*args, **kwargs, fg = "black", padx = 10, pady = 10)
        # btn["font"] = self.window.FONT
        return btn

    ## Micellanous Methods ##

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)  

    # Focuses cursor on passed entry widget
    def focus_cursor(self, entry):
        entry.focus_set()
    
     ## Window Methods ##
        
    def introduce(self):
        self.newWindow()
        self.linkReturn(self.query1)
             
        text = "Welcome to Venue Planer!"
        self.label(self.window, text = text).pack(pady = (100, 50))
        
        text = "This application automatically assigns guests to seats based on information provided."
        self.label(self.window, text = text).pack(pady = 50)
        
        text = "Press enter to continue"
        self.label(self.window, text = text).pack(pady = 50)
        
        tk.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newWindow()
        # self.newForm()
        self.linkReturn(self.query2)

        text = "enter the number of seats per table:"
        self.label(text = text).pack(pady = (100, 0))

        self.entry().pack(pady = 25)
        
        text = "Press enter to continue"
        self.label(self.window, text = text).pack(pady = 50)

        tk.mainloop()

    # queries for 
    def query2(self, event = None):
        self.newWindow()
    
    # querys for
    def query3(self):
        pass

def main():
    global bg
    bg = bg.Background()
    global gui
    gui = Gui()

if __name__ == "__main__":
    main()
