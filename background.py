class Background:
    def __init__(self):
        self.venues = list()
    def add_venue(self, venue):
        self.venues.append(venue)

class Venue():
    def __init__(self, name):
        self.name = name
        self.tables = list()
        self.groups = list()
    def add_table(table):
        self.tables.add(table)
    def set_name(name):
        self.name = name
    def get_name():
        return self.name

class Group():
    def __init__(self):
        self.persons = list()
    def get_num_persons():
        return len(self.persons)
    def add_person(person):
        self.persons.add(person)
    
class Table():
    def __init__(self, name):
        self.name = name
        self.persons = list()
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_num_persons(self):
        return len(self.persons)
    def add_person(self, person):
        self.persons.add(person)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age              # to do: assign persons of similar age group to same tables
                                    # to do: make list of persons not allowed at the same table