class Venue:
	def __init__(self):
		self.tables = []
		self.people = []

	def add_table(self, table):
		self.tables.append(table)

	def remove_table(self, table):
		self.tables.remove(table)
		
	def get_table(self, index):
		return self.tables[index]

	def add_person(self, person):
		self.people.append(person)
	
	def remove_person(self, person):
		self.people.remove(person)

	def get_num_tables(self):
		return len(self.tables)
