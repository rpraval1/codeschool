"""
:Author: Pravallika
:Description: Given an array of citations (each citation is a non-negative integer) of a researcher,
                write a function to compute the researcher's h-index.

                According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each,
                and the other N − h papers have no more than h citations each."
:Explanation:
		Given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
        Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
"""

class HIndex(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h

obj = HIndex()

citations = [3, 0, 6, 1, 5]
print(obj.hIndex(citations))
