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
		myList = []
		myListLength = len(myList)
		for currChar in myString:
			if currChar in parentheses:
				myList.append(currChar)
			elif  myListLength != 0 or parentheses[myList.pop()] != currChar:
				return False
		if myListLength == 0:
			return True
	
validPar = ValidParentheses()
myString = '{[(]]}'
print(validPar.isValid(myString))
