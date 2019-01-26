class_times = [(0,50),(30,75),(60,150)]


class Solution:
	def get_min_needed_rooms(self, times): 
		startTimes = []
		endTimes = [] 

		for class_time in class_times: 
			startTimes.append(class_time[0])
			endTimes.append(class_time[1])


print("The minimum number of classes needed is: %d" % (Solution()).get_min_needed_rooms(class_times))