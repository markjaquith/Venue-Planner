import unittest
from venueplanner.Table import *
from venueplanner.Person import *

class TestStringMethods(unittest.TestCase):
	def setUp(self):
		self.archimedes = Person("Archimedes", "12")
		self.socrates = Person("Socrates", "24")

	def test_empty_table(self):
		table = Table(0)
		self.assertRaises(Exception, table.add_person, self.archimedes)

	def test_full_table(self):
		# Create a table with one seat
		table = Table(1)

		# Add a person to the table
		table.add_person(self.archimedes)

		# Assert that the table is full
		self.assertTrue(table.is_full())

		# Try to add another person to the table, which should raise an exception
		self.assertRaises(Exception, table.add_person, self.socrates)

	def test_not_full_table(self):
		table = Table(2)
		table.add_person(self.archimedes)

		# At this point, the table has one person at it, so it should not be full
		self.assertFalse(table.is_full())

		# Now we add a second person to the table, making it full
		table.add_person(self.socrates)

		# Is it full? It should be.
		self.assertTrue(table.is_full())

	def test_remove_person(self):
		table = Table(1)
		table.add_person(self.archimedes)
		table.remove_person(self.archimedes)
		self.assertFalse(table.is_full())

	def test_add_the_same_person_twice(self):
		table = Table(2)
		table.add_person(self.archimedes)
		self.assertRaises(Exception, table.add_person, self.archimedes)

if __name__ == '__main__':
    unittest.main()