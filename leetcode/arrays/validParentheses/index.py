"""
:Author: Pravallika
:Description: Given a string containing just the characters '(',')','{','}','[',']', determine if input string is valid
:Explanation: "()" and "()[]{}" are valid "(}]" and "[}" are not valid
"""

class ValidParentheses(object):
	def isValid(self, myString):
		"""
		:type myString: str
		:rtype: bool
		"""
		parentheses = {'(':')', '[':']', '{':'}'}
		openPar = []

		for currChar in myString:
			if currChar in parentheses:
				openPar.insert(0,currChar)
			else:
				if len(openPar) == 0:
					return False
				if parentheses[openPar[0]] != currChar:
					return False
				else:
					openPar.pop(0)
		if len(openPar) > 0:
			return False
		return True





validPar = ValidParentheses()
myString = '['
print(validPar.isValid(myString))
