"""
:Author: Pravallika
:Description: Given two binary strings, return their sum (also a binary string).
:Explanation: For example,
	a = "11"	
	b = "1"
	Return "100".
"""

class AddBinary(object):
	def addBinary(self, a, b):
		"""
        	:type a: str
        	:type b: str
        	:rtype: str
        	"""
		if a == "0" and b == "0":
			return a
		if a == "0":
			return b
		if b == "0":
			return a
		a = a[::-1]
		b = b[::-1]
        
		numA = 0 
		numB = 0
		for i in range(len(a)):
			numA = numA+(pow(2,i)*int(a[i]))
        
		for i in range(len(b)):
			numB = numB + (pow(2,i)*int(b[i]))
        
		sum = numA + numB
		val = sum
		result = ''
		while val != 1:
			rem = val%2
			val = val//2
			result = result + str(rem)
			if val == 1:
				result = result + str(val)
        
		return result[::-1]

print(AddBinary().addBinary("111","1"))
