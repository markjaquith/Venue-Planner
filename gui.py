
import tkinter as tk
# import tkinter.font as font'

import background

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
        return btn

    ## Micellanous Methods ##

    # Assigns key "Return" to run subsequent window method.
    def linkReturn(self, next_func):
        self.window.bind("<Return>", next_func)  

    # Focuses cursor on passed entry widget
    def focusCursor(self, entry):
        entry.focus_set()
    
    #checks to make sure user entered information into a specific Entry()
    def isEntered(self, entry):
        if entry.get(): return True
        return False


     ## Window Methods ##
        
    def introduce(self):
        self.newWindow()
        self.linkReturn(self.query1)
             
        text = "Welcome to Venue Planer!"
        self.label(self.window, text = text).pack(pady = (100, 50))
        
        text = "This application automatically assigns guests to seats based on information provided."
        self.label(self.window, text = text).pack(pady = 50)
        
        text = "To begin enter the name of your venue:"
        self.label(text = text).pack(pady = 10)

        entry = self.entry()
        entry.pack(pady = 10)
        self.focusCursor(entry)

        bg.addVenue(Venue())
        # for venue in bg.venues: print("successful!")


        text = "Press enter to continue"
        self.label(self.window, text = text).pack(pady = 50)
        
        tk.mainloop()

    # querys for max seats per table
    def query1(self, event = None):
        self.newWindow()
        self.linkReturn(self.query2)

        text = "For starters, please enter the name of your venue:"
        self.label(text = text).pack(pady = 50)

        entry = self.entry()
        entry.pack(pady = 25)
        self.focusCursor(entry)
        bg.addVenue(entry)

        text = "Press enter to continue"
        self.label(self.window, text = text).pack(pady = 50)

        tk.mainloop()

    # queries for max people per table
    def query2(self, event = None):
        self.newWindow()

        text = "enter the max number of seats per table:"
        self.label(text = text).pack(pady = (100, 0))

        entry = self.entry()
        entry.pack(pady = 25)
        entry.focus_set()

        tk.mainloop()

    # querys for
    def query3(self):
        pass

class Background:
    def __init__(self):
        self.venues = list()
    def addVenue(self, venue):
        self.venues.append(venue)

class Venue:
    def __init__(self):
        self.name = None
        self.maxSeats = 0
        self.tables = list()
        self.groups = list()
    def addTable(table):
        self.tables.append(table)
    def addGroup(group):
        self.groups.append(group)

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

def main():
    global bg
    bg = Background()
    global gui
    gui = Gui()

if __name__ == "__main__":
    main()
