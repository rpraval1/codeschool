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
		
		tempFreq = {}
		ptr1 = 0
		result = ''

		for i,c in enumerate(s):
			if c in tFreq:
				tempFreq[c] = tempFreq.get(c,0)+1
				if tempFreq[c] > tFreq[c]:
					ptr += 1
					i = ptr1
					tempFreq = {}
			print(tempFreq)
			if tempFreq == tFreq:
				print(tempFreq)
				if result == '':
					result = s[ptr1:i+1]
				elif len(result) > len(s[ptr1:i+1]):
					result = s[ptr1:i+1]
				ptr1 = ptr1 + 1
				i = ptr1
				tempFreq = {}
		print(result)
		
minWindow = MinWindow()
minWindow.minWindowSubstring("ADOBECODEBANC","ABC")
	
