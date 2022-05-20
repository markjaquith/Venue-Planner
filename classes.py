from this import d
import tkinter as tk

class Venue:
    def __init__(self):
        self.name = "default name"
        self.tables = set()
    def add_table(table)
        self.tables.add(table)
    def set_name(name):
        self.name = name
    def get_name():
        return self.name
    
class Table(Venue):
    def __init__(self):
        self.number = 0
        self.num_persons = 0        #Number of persons
        self.obj_persons = set()    #Person objects
    def set_number(num):
        self.number = num
    def get_numbers(num):
        return self.number
    def set_num_persons(num):
        self.persons = num
    def get_num_persons():          #gets number of persons
        return self.persons
    def add_obj_persons(person):    #adds person object
        person.add(person)
        

class Person(Table):
    def __init__(self):
        print("test")