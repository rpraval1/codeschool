"""
:Author: Pravallika
:Description: Check if a given string is palindrome, considering only alphanumeric characters ignoring cases.
:Example: "A man, a plan, a canal: Panama" is a palindrome.     "race a car" si not a palindrome
"""
import re
class Palindrome(object):
	def isPalindrome(self, S):
		"""
		:type S: str
		:rtype: bool
		"""
		if S == '':
			return True
		
		alphaNumStr = ''.join(re.findall("[a-zA-Z0-9]+",S))
		alphaNumStr = alphaNumStr.lower()

		j = len(alphaNumStr)-1
		
		for i in range(len(alphaNumStr)):
			if alphaNumStr[i] != alphaNumStr[j]:
				return False
			j = j-1
		
		return True


palindrome = Palindrome()
S = "A man, a plan, a canal: Panama"
print(palindrome.isPalindrome(S))
