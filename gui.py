from distutils.log import info
import tkinter as tk
# import tkinter.font as font'

class Gui:
    def __init__(self):
        self.entries = list()
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

    def entry(self, isFirst, *args, **kwargs):
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
        self.venue = Venue(self.entry_widget.get())
        info.addVenue(self.venue)
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

        text = "Enter in the names of people who must be together, such as a Mom and her kids (one group per page)"
        self.label(text = text).pack(pady = 25)

        self.entries.append(self.entry(True))
        for x in range(self.max_seats - 1):
            self.entries.append(self.entry(False))
        print(self.entries)

        # for entry in self.entries:
        #     print(entry.get())

        text = "Only click continue once you've entered all of the groups"
        self.label(text = text).pack(pady = 25)

        self.button(text = "back", command = self.query2).pack(side = "left")        
        self.linkReturn(self.query3)
        self.button(text = "Continue", command = self.query4).pack(side = "right")

        
        for entry in self.entries:
            info.people.append(Person(entry.get()))
        for person in info.people:
            print(person.name)

        self.entries.clear()

        tk.mainloop()
        
#len = length of entries filled out.

    def query4(self):
        self.newWindow()
        self.label(text = "test")

class Info:
    def __init__(self):
        self.venues = list()
        self.groups = list()
        self.tables = list()
        self.people = list()
    def addVenue(self, venue):
        self.venues.append(venue)

class Venue:
    def __init__(self, name):
        self.name = name

class Group():
    def __init__(self):
        pass

class Person:
    def __init__(self, name):
        self.name = name
        self.group = Group()
        self.age = None

        # to do: assign persons of similar age group to same tables
        # to do: make list of persons not allowed at the same table


    

if __name__ == "__main__":
    global info
    info = Info()
    global gui
    gui = Gui()