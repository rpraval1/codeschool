"""
:Author: Pravallika
:Description: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
		find the minimum number of conference rooms required.
:Explanation: 
		For example,
		Given [[0, 30],[5, 10],[15, 20]],
		return 2.
"""

class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	
class Meeting(object):
	def needRoom(self, intervals):
		"""
		:type intervals: List[Inteval]
		:rtype: int

		"""
		
		start = []
		end = []
		
		for i in intervals:
			start.append(i.start)
			end.append(i.end)
		
		start.sort()
		end.sort()
		
		available = 0
		newRooms = 0
	
		s=0
		e=0
		
		while s< len(start):
			if start[s] < end[e]:
				if available == 0:
					newRooms += 1
				else:
					available -= 1
				s = s+1
			else:
				available += 1
				e = e+1
		
		return newRooms
	

print(Meeting().needRoom([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]))
