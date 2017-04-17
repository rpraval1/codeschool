"""
:Author: Pravallika
:Description: Given two sparse matrices A and B, return the result of AB.

		You may assume that A's column number is equal to B's row number.
:Explanation: A = [
  			[ 1, 0, 0],
  			[-1, 0, 3]
		]
		
		B = [
  			[ 7, 0, 0 ],
  			[ 0, 0, 0 ],
  			[ 0, 0, 1 ]
		]

		     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
		AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  		  | 0 0 1 |

"""

class Multiply(object):
	
	def sparseMultiply(self, A, B):
		
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		"""
		
		m = len(A)
		n = len(A[0])
		l = len(B[0])

		result = [[0 for i in range(l)] for j in range(m)]

		for i in range(m):
			for k in range(n):
				if A[i][k]:
					for j in range(l):
						result[i][j] += A[i][k] * B[k][j]

		return result


obj = Multiply()
A = [[-1,0,0], [-1,0,3]]
B = [[7,0,0,], [0,0,0], [0,0,1]]

print(obj.sparseMultiply(A, B))


