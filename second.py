import math
import json
from operator import itemgetter

class Second():
	""" Class to identify friends within some distance """

	def __init__(self):
		self.friends_data = []
		self.friends_to_invite_data = []
		self.SOURCE_LOCATION = [float(12.9611159), float(77.6362214)]
		self.INVITATION_DISTANCE = 101
		self.EARTH_RADIUS = 6371

	def calculateDistance(self, friends_location):
		lat_dest = friends_location[0]
		long_dest = friends_location[1]
		lat_source = self.SOURCE_LOCATION[0]
		long_source = self.SOURCE_LOCATION[1]

		phy_1 = math.radians(lat_source)
		phy_2 = math.radians(lat_dest)
		delta_lambda = math.radians(long_dest - long_source)
		delta_sigma = math.acos((math.sin(phy_1) * math.sin(phy_2)) + (math.cos(phy_1) * math.cos(phy_2) * math.cos(delta_lambda)))

		dist = self.EARTH_RADIUS*delta_sigma
		return dist

	def loadData(self):
		with open('friends.json', 'r') as data:
			json_data = data.read()
		
		self.friends_data = json.loads(json_data)

	def preparingFriendsList(self):
		# load Data from json file
		self.loadData()
		self.friends_to_invite_data = []
		for friend in self.friends_data:
			dist = self.calculateDistance([float(friend.get('latitude')), float(friend.get('longitude'))])
			if dist < self.INVITATION_DISTANCE:
				self.friends_to_invite_data.append({'user_id': friend.get('user_id'), 'name': friend.get('name')})

		self.friends_to_invite_data = sorted(self.friends_to_invite_data, key = itemgetter('name'))
		print(self.friends_to_invite_data)

	