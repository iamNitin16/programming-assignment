import unittest
from second import Second

class TestSuiteForSecond(unittest.TestCase):
	""" Test for Second Program """

	obj = Second()

	def testCONSTANTS(self):
		self.assertEqual(self.obj.SOURCE_LOCATION, [float(12.9611159), float(77.6362214)])
		self.assertEqual(self.obj.INVITATION_DISTANCE, 101)
		self.assertEqual(self.obj.EARTH_RADIUS, 6371)

	def testCalculateDistanceFunc(self):
		dist = self.obj.calculateDistance([float(12.9611159), float(77.6362214)])
		self.assertEqual(dist, 0)

	def testLoadData(self):
		self.obj.loadData()
		self.assertEqual(len(self.obj.friends_data), 32)

	def testPreparingFriendsList(self):
		self.obj.preparingFriendsList()
		self.assertEqual(len(self.obj.friends_to_invite_data), 11)

if __name__ == '__main__':
	unittest.main()