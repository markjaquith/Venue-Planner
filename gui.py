
import tkinter as tk
# import tkinter.font as font'

import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.widgets = list()
        self.frames = list()
        self.introduce()

    # closes current window and opens the next window.
    def newForm(self):    
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        for frame in self.frames:
            frame.grid_forget()
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)        

    ## WIDGET METHODS ##

    def label(self, *args, **kwargs):
        label = tk.Label(*args, **kwargs, bg = "blue", fg = "white")
        self.widgets.append(label)
        return label

    def entry(self, *args, **kwargs):
        entry = tk.Entry(*args, **kwargs)
        self.widgets.append(entry)
        return entry

    # Focuses cursor on passed entry widget
    def focus_cursor(self, entry):
        entry.focus_set()

    def button(self, *args, **kwargs):
        btn = tk.Button(*args, **kwargs, fg = "black", padx = 10, pady = 10)
        # btn["font"] = self.window.FONT
        self.widgets.append(btn)
        return btn



    #creates a grid for frames to be placed.
    def create_grid(self, x, y):
        for x in range(x):
            for y in range(y):
                self.window.columnconfigure(x, weight = 1)
                self.window.rowconfigure(y, weight = 1)

    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newForm()
        self.linkReturn(self.query1)
             
        text = "Welcome to Venue Planer!"
        self.label(text = text).pack(pady = (100, 50))
        
        text = "This application automatically assigns guests to seats based on information provided."
        self.label(text = text).pack(pady = 50)
        
        text = "Press enter to continue"
        self.label(text = text).pack(pady = 50)
        
        tk.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newForm()
        text = "enter the number of seats per table:"
        self.label(text = text).pack(pady = 100)

        # self.entry().pack(pady = ())

    # queries for 
    def query2(self, event = None):
        self.newForm()
    
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
