"""
:Author: Pravallika
:Description: Given a collection of intervals, merge all overlapping intervals.
:Explanation: For example,
		Given [1,3],[2,6],[8,10],[15,18],
		return [1,6],[8,10],[15,18].
"""

class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

	def __repr__(self):
		if self:
			return "[{}, {}]".format(self.start, self.end)

class MergeIntervals(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		if not intervals:
			return intervals
		
		intervals.sort(key=lambda x: x.start)
		result = [intervals[0]]
		
		for i in range(len(intervals)):
			prev = result[-1]
			curr = intervals[i]
			
			if curr.start <= prev.end:
				prev.end = max(prev.end, curr.end)
			else:
				result.append(curr)
		return result


print(MergeIntervals().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))
