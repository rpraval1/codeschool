"""
:Author: Pravallika
:Description: Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""

class HIndexII(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)

        left = 0
        right = n-1

        while left <= right:
            mid = (left + right)//2

            if citations[mid]>=n-mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left

obj = HIndexII()

citations = [0,1,3,5,6]
print(obj.hIndex(citations))
