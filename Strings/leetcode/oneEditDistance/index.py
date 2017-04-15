"""
:Author: Pravallika
:Description: Given two strings S and T, determine if they are both one edit distance apart.
"""


class OneEdit(object):
	def findOneEdit(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
				
		if len(S)-len(T) > 1:
			return False
	
		if len(T) > len(S):
			self.findOneEdit(T,S)
		
		i = 0
		shift = len(T)-len(S)
		
		while i < len(S) and S[i] == T[i]:
			i = i+1
		
		if shift == 0:
			i = i+1
		while i < len(S) and S[i] == T[i+shift]:
			i = i+1
		
		return i==m
	

obj = OneEdit()
S = "teacher" 
T = "acher"
print(obj.findOneEdit(S,T))  
