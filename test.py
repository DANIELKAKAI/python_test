import unittest

from example import add,multiply,even

class ExampleTest(unittest.TestCase):
	def test_even(self):
		self.assertTrue(even(2),"even")
	def test_add(self):
		self.assertEqual(add(2,3),5,"adding")
	def test_multiply(self):
		self.assertEqual(multiply(3,4),12,"multiplying")


if __name__=="__main__":
	unittest.main()






