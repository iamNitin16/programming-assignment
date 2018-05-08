
class First():
	''' class for finding triplet of given sum '''

	def __init__(self, data, sum_of_three):
		self.data = data
		self.sum_of_three = sum_of_three
		self.triplet = []

	def findTriplet(self):
		self.triplet = []
		# Sort the data
		self.data.sort()
		data_size = len(self.data)
		#fixing the one element of triplet and changing the others
		for first_elem_index in range(0, data_size):
			# other two elements of triplet have index j and k
			second_elem_index = first_elem_index + 1
			third_elem_index = data_size - 1

			while( second_elem_index < third_elem_index ):
				if (self.data[first_elem_index] + self.data[second_elem_index] + self.data[third_elem_index] == self.sum_of_three): 
					self.triplet.append(self.data[first_elem_index])
					self.triplet.append(self.data[second_elem_index])
					self.triplet.append(self.data[third_elem_index])
					break
				elif (self.data[first_elem_index] + self.data[second_elem_index] + self.data[third_elem_index] < self.sum_of_three):
					second_elem_index += 1
				else:
					third_elem_index -= 1
