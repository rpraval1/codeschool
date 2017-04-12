"""
:Author: Pravallika
:Description: find minimum window substring in s which will contain all the characters in t
:Example: s = "ADOBECODEBANC" t = "ABC" Minimum window is "BANC"
"""
 
class MinWindow(object):
	def minWindowSubstring(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		
		tFreq = {}
		for c in t:
			tFreq[c] = tFreq.get(c,0)+1
		
		tempFreq = tFreq.copy()
		ptr1 = 0
		result = ''

		for i,c in enumerate(s):
			print(tempFreq)
			if c in tempFreq:
				if tempFreq[c] >= 1:
					tempFreq[c] -= 1
				else:
					ptr1 += 1
					i = ptr1
					tempFreq = tFreq.copy()
			
			if all(value == 0 for value in tempFreq.values()):
				print(s[ptr1:i+1])
				if result == '':
					result = s[ptr1:i+1]
				elif len(result) > len(s[ptr1:i+1]):
					result = s[ptr1:i+1]
				ptr1 = ptr1 + 1
				i = ptr1
				tempFreq = tFreq.copy()
		print(result)
		
minWindow = MinWindow()
minWindow.minWindowSubstring("ADOBECODEBANC","ABC")
	
