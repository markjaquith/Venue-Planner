import tkinter as tk
# import tkinter.font as font'

class Gui:
    def __init__(self):
        self.venue = None
        self.entry_widget = None
        self.window = tk.Tk()
        self.introduce()

    # creates a new Venue object and opens a new window.
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

    def entry(self, isFirst):
        self.entry_widget = tk.Entry()
        self.entry_widget.pack()
        if isFirst:
            self.entry_widget.focus_set()
        return self.entry_widget

    def button(self, *args, **kwargs):
        btn = tk.Button(*args, **kwargs, fg = "black", padx = 10, pady = 10)
        return btn        

    ## Micellanous Methods ##

    def back(self, next_func):
        self.button(text = "back", command = next_func).pack(side = "left")

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)  

    # Focuses cursor on passed entry widget
    def focusCursor(self, entry):
        entry.focus_set()
    
     ## Window Methods ##
        
    def introduce(self):
        self.newWindow()

        text = "Welcome to Venue Planer!"
        self.label(self.window, text = text).pack(pady = (100, 50))
        
        text = "This application automatically assigns guests to seats based on information provided."
        self.label(self.window, text = text).pack(pady = 50)

        text = "To begin enter the name of your venue:"
        self.label(text = text).pack(pady = 10)

        self.entry(True)
        
        text = "Press enter to continue"
        self.label(self.window, text = text).pack(pady = 50)
        self.linkReturn(self.query1)

        tk.mainloop()
    
    # querys for max seats per table
    def query1(self, event = None):
        bg.addVenue(Venue(self.entry_widget.get()))
        self.newWindow()

        text = "Enter the max number of seats per table as an integer:"
        self.label(text = text).pack(pady = 50)

        self.entry_widget = tk.Entry()
        self.entry_widget.pack()
        self.focusCursor(self.entry_widget)

        self.button(text = "back", command = self.introduce).pack(side = "left")
        
        self.linkReturn(self.query2)
        tk.mainloop()

    # queries for number of tables
    def query2(self, event = None):
        self.max_seats = int(self.entry_widget.get())
        self.newWindow()

        text = "Enter max number of tables:"
        self.label(text = text).pack(pady = (100, 10))

        self.entry_widget = self.entry(True)

        self.button(text = "back", command = self.query1).pack(side = "left")
        self.linkReturn(self.query3)
        tk.mainloop()

    # querys for group
    def query3(self, event = None):
        self.newWindow()

        text = "Enter in the names of people who must be together. (one group per page)"
        self.label(text = text).pack(pady = 25)
        
        self.entry(True)
        for x in range(self.max_seats): #to do: store maxSeats
            self.entry(False)

        self.button(text = "back", command = self.query1).pack(side = "left")        
        self.linkReturn(self.query4)
        tk.mainloop()

    def query4(self):
        self.newWindow()
        self.label(text = "test")

class Background:
    def __init__(self):
        self.venues = list()
    def addVenue(self, venue):
        self.venues.append(venue)

class Venue:
    def __init__(self, name):
        self.name = name
        self.max_seats = 0
        self.tables = list()
        self.groups = list()

class Group:
    def __init__(self):
        self.persons = list()
    def addPerson(person):
        self.persons.add(person)
    
class Table:
    def __init__(self, name):
        self.persons = list()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age              # to do: assign persons of similar age group to same tables
                                    # to do: make list of persons not allowed at the same table


    

if __name__ == "__main__":
    global bg
    bg = Background()
    global gui
    gui = Gui()