"""
:Author: Pravallika
:Description: Given a digit string, return all possible letter combinations that the number could represent.
:Explanation: Input:Digit string "23"
		Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class LetterComb(object):
	def printLetterComb(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		
		if not digits:
			return []
		
		digitDict = {0: '', 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
		
		result = [""]

		for digit in reversed(digits):
			option = digitDict[int(digit)]
			
			m = len(option)
			n = len(result)
			result += [result[i%n] for i in range(n,m*n)]
			
			for i in range(m*n):
				result[i] = option[i//n] + result[i]
		
		return result


digit = "23"

print(LetterComb().printLetterComb(digit))
