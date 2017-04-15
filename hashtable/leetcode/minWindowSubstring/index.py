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
		
		expectCount = [0]*52
		currCount = [0]*52
		
		for c in t:
			expectCount[ord(c)-ord('a')] += 1

		i = 0
		count = 0
		start = 0
		minWidth = float("inf")
		minStart = 0
		
		while i<len(s):
			currCount[ord(s[i])-ord('a')] += 1
			
			if currCount[ord(s[i])-ord('a')] <= expectCount[ord(s[i])-ord('a')]:
				count += 1
			
			if count == len(t):
				while expectCount[ord(s[start])-ord('a')]==0 or currCount[ord(s[start])-ord('a')] > expectCount[ord(s[start])-ord('a')]:
					currCount[ord(s[start])-ord('a')] -= 1
					start += 1
				
				if minWidth > i-start+1:
					minWidth = i-start+1
					minStart = start		
		

			i = i+1
			
		if minWidth == float("inf"):
			return ""
		
		return s[minStart:minStart + minWidth]
		
			
obj = MinWindow()
s = "ADOBECODEBANC"
t = "ABC"
print(obj.minWindowSubstring(s,t)) 
