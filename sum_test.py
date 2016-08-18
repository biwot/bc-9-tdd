import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):
	def setUp(self):
		self.numbers= [10, 5, 7, 8, 90, 60]
		self.strings=["5", "10", "7", "A", "B", "a"]

	def test_sum_of_numbers(self):
		
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(my_sum(10, 15), 25)

	def test_list_of_strings(self):
		self.assertEqual(my_sum("5", "10"), "Input not operable")
		self.assertEqual(my_sum("A", "")) ,"Input not operable")

	def test_list_of_mixed_input(self):
		self.assertequal(my_sum(5, "10")), "Input not operable")
		
		



if __name__== '__main__':
	unittest.main()