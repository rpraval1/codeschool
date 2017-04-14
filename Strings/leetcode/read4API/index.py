"""
:Author: Pravallika
:Description: The API: int read4(char *buf) reads 4 characters at a time from a file.

		The return value is the actual number of characters read. 
		By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
"""

def read4(buf):
	global fileContent
	
	i = 0
	while i<len(fileContent) and i<4:
		buf[i] = fileContent[i]
		i =i+1
	if len(fileContent) > 4:
		fileContent = fileContent[4:]
	else:
		fileContent = ""

	return i

class ReadContent(object):
	def read(self, buf, n):
		"""
		:type buf: List[str]
		:type n: Maximum number of characters to read
		:rtype: Number of characters read
		"""
		numRead = 0
		tempBuff = [""]*4

		for i in range(n//4+1):
			size = read4(tempBuff)
			if size:
				buf[numRead:numRead+size] = tempBuff
				numRead = numRead+size
			else:
				break
		return min(numRead, n)


obj = ReadContent()
global fileContent
fileContent = "Read my Content"
buf = ['' for c in range(100)]
print(buf[:obj.read(buf,3)])
print(buf[:obj.read(buf,4)])
