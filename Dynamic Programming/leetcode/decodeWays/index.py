"""
:Author: Pravallika
:Description: A message containing letters from A-Z is being encoded to numbers using the following mapping:

		'A' -> 1
		'B' -> 2
		...
		'Z' -> 26
		Given an encoded message containing digits, determine the total number of ways to decode it.

:Explanation: For example,
		
		Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

		The number of ways decoding "12" is 2.
"""

class Decode(object):

	def decodeWays(self, s):
		
		"""	
		:type s: str
		:rtype: int
		"""
		
		if s == '' or s[0] == '0':
			return 0

		counter = 1
		prevCounter = 0

		for i in range(len(s)):
			temp = 0
			
			if s[i] != '0':
				temp = counter

			if (i>0 and (s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'))):
				temp += prevCounter

			prevCounter = counter
			counter = temp


		return counter



obj = Decode()
s = '143021'

print(obj.decodeWays(s))

