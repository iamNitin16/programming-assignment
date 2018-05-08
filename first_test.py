import unittest
from first import First

class TestSuiteForFirst(unittest.TestCase):
	""" Tesing the First Class """

	obj = First([1, 4, 45, 5, 10, 8], 22)

	def testClassInit(self):
		self.assertEqual(self.obj.data, [1, 4, 45, 5, 10, 8])
		self.assertEqual(self.obj.sum_of_three, 22)
		self.assertEqual(self.obj.triplet, [])

	def testTripletFunc(self):
		self.obj.data = [1, 4, 45, 5, 10, 8]
		self.obj.sum_of_three = 22
		self.obj.findTriplet()
		self.assertEqual(sum(self.obj.triplet), 22)

	def testEmptyTripletData(self):
		self.sum_of_three = 23
		self.assertEqual(self.obj.triplet, [])

	def testNegativeData(self):
		self.obj.data = [-1, -2, -3, -4]
		self.obj.sum_of_three = -6
		self.obj.findTriplet()
		self.assertEqual(sum(self.obj.triplet), -6)

	

if __name__ == '__main__':
	unittest.main()