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
		
		for i,c in enumerate(s):
			if c in tFreq:
				tempFreq[c] = tempFreq.get(c,0)+1
			print(tempFreq)
			if tempFreq == tFreq:
				print(tempFreq)
				ptr1 = ptr1 + 1
				i = ptr1
				tempFreq = {}

minWindow = MinWindow()
minWindow.minWindowSubstring("ADOBECODEBANC","ABC")
	
