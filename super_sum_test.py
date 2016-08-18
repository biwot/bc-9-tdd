import unittest

from super_sum import super_sum

class SuperSumTest(unittest.TestCase):
	
	def test_sum_of_even_numbers(self):		
		self.assertEqual(super_sum([2, 4,6 ,8]), 20)
		self.assertEqual(super_sum([44, 66,88, 98], 296)

	def test_sum_of_odd_numbers(self):
		self.assertEqual(super_sum([3, 9, 15, 27], 54)
		self.assertEqual(super_sum([5, 7, 13, 17], 42)

	def test_list_of_mixed_elements(self):
		self.assertequal(super_sum([[1, 2, 3], 4, 5, 6]), 21)
		self.assertequal(super_sum([22, 11, [13, 17, 19] 7), 89)

	def test_list_of_negative_numbers(self):
		self.assertequal(super_sum([-1, -5, -5, -7, -9]), -27)
		self.assertequal(super_sum([[1, 2, 3], 4, 5, 6]), 21)

	def test_list_of_strings(self):
		self.assertequal(super_sum([["lol", "huh", "gee", "foo"]), 0)
		self.assertequal(super_sum([[1, 2, 3], ["lol", "huh", "foo"]), 0)

if __name__== '__main__':
	unittest.main()