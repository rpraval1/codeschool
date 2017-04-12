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
		openLen = len(openPar)
		closedCount = 0

		for currChar in myString:
			if currChar in parentheses:
				openPar.append(currChar)
			if currChar in parentheses.values():
				closedCount += 1

		if openLen != closedCount:
			return False
		else:
			for currChar in parentheses:
				if currChar in openPar:
					continue
				else:
					if parentheses[openPar.pop()] != currChar:
						return False
		if openLen == 0:
			return True





validPar = ValidParentheses()
myString = '['
print(validPar.isValid(myString))
