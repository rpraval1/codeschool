"""
:Author: Pravallika
:Description: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
		You may assume the dictionary does not contain duplicate words.
:Explanation: For example, given
		s = "leetcode",
		dict = ["leet", "code"].

		Return true because "leetcode" can be segmented as "leet code".
"""
class WordBreak(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		stringLen = len(s)
		
		maxLen = 0
		for word in wordDict:
			maxLen = max(maxLen, len(word))
		
		canBreak = [False]*(stringLen+1)
		canBreak[0] = True

		for i in range(1,stringLen+1):
			for l in range(1, min(i,maxLen)+1):
				if canBreak[i-l] and s[i-l:i] in wordDict:
					canBreak[i] = True

		return canBreak[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(WordBreak().wordBreak(s,wordDict))
