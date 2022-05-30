class Table:
	def __init__(self, num_seats):
		self.num_seats = num_seats
		self.people = []

	def add_person(self, person):
		if (self.is_full() or self.person_is_in_table(person)):
			raise Exception("Error")
		self.people.append(person)

	def remove_person(self, person):
		self.people.remove(person)

	def is_full(self):
		return len(self.people) == self.num_seats
	
	def person_is_in_table(self, person):
		return person in self.people