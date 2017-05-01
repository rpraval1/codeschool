"""
:Author: Pravallika
:Description: Given the words in the magazine and the words in the ransom note, print Yes if ransom note exactly uses whole words from the magazine; 
		otherwise, print No.
:Explanation: give me one grand today night
		give one grand today
		
		Answer: Yes

"""

def ransomNote(magazine, ransom):
	magazineDict = {}
	ransomDict = {}
	
	for word in magazine:
		magazineDict[word] = magazineDict.get(word,0)+1     
	for word in ransom:
		ransomDict[word] = ransomDict.get(word,0)+1
	for word in ransomDict:
		if ransomDict[word] > magazineDict[word]:
			return False
	return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransomNote(magazine, ransom)
if(answer):
	print("Yes")
else:
	print("No")

