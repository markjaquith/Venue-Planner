
import tkinter as tk
import tkinter.font as font
import background as bg

class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.widgets = list()
        self.frames = list()
        self.introduce()

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)
    # closes current window and opens the next window. also executes ^linkReturn()^.
    def newForm(self, func):
        for widget in self.widgets:
            widget.destroy()
        # for frame in self.frames:
        #     frame.pack_forget(
        #     frame.destroy()
        #     )
        self.widgets.clear()
        # self.window.FONT = font.Font(size = 20)
        self.window.configure(bg = "blue")
        self.window.title("Venue Planner")
        self.window.geometry("800x600")
        self.linkReturn(func)

    ## WIDGET METHODS ##

    def label(self, *args, **kwargs):
        label = tk.Label(*args, **kwargs, bg = "blue", fg = "white")
        self.widgets.append(label)
        return label

    def entry(self, *args, **kwargs):
        entry = tk.Entry(*args, **kwargs)
        self.widgets.append(entry)
        return entry

    def button(self, *args, **kwargs):
        btn = tk.Button(*args, **kwargs, fg = "black", padx = 10, pady = 10)
        # btn["font"] = self.window.FONT
        self.widgets.append(btn)
        return btn

    def frame(self, *args, **kwargs):
        frame = tk.Frame(*args, **kwargs, fg = "blue")
        # frame.configure(background = "blue", foreground = "blue")
        self.frames.append(frame)
        # frame.configure(bg = "blue", fg = "blue")
    
    # Focuses cursor on passed entry widget argument
    def focus_cursor(self, entry):
        entry.focus_set()

    def grid(self, x, y):
        for x in range(x):
            self.window.columnconfigure(x)
        for y in range(y):
            self.window.rowconfigure(y)

    # Displays opening message and querys for venue name.
    def introduce(self):
        self.newForm(self.query1)
        text = "Welcome to Venue Planer!"
        self.label(text = text, pady = 50).pack()
        text = "This application automatically assigns your guests to seats based on information provided."
        self.label(text = text, pady = 50).pack()

        text = "To start enter the name of your venue:"
        self.label(text = text).pack()
        entry = self.entry()
        entry.pack()
        
        self.focus_cursor(entry)
        self.label(text = "press or click enter to continue:", pady = 10).pack()
        self.button(text = "Enter", command = self.query1).pack()
        tk.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newForm(self.query2)
        # self.grid(0)
        self.label(text = "how many seats are there per table?", pady = 25).pack()
        self.label(text = "Please enter an integer:").pack()
        entry = self.entry()
        entry.pack()
        self.focus_cursor(entry)
        self.button(text = "Submit", command = self.query2).pack()
        
    # queries for 
    def query2(self, event = None):
        self.newForm(self.query3)
    
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
