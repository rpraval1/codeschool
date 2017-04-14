"""
:Author: Pravallika
:Description: read called multiple times
"""

def read4(buf):
	global fileContent
	i = 0
	while i < len(fileContent) and i<4:
		buf[i] = fileContent[i]
		i = i+1
	
	if len(fileContent)>4:
		fileContent = fileContent[4:]
	else:
		fileContent = ""
	return i


class ReadContent(object):
	def __init__(self):
		self._buf4=['']*4
		self._i4 = 0
		self._n4 = 0

	def read(self,buf, n):
		"""
		:type buf: Destination buffer(List[str])
		:type n: Maximum number of characters to read(int)
		:rtype: The number of characters read(int)
		"""
		i = 0
		while i<n:
			if self._i4 < self._n4:
				buf[i] = self._buf4[self._i4]
				i = i+1
				self._i4 += 1
			else:
				self._n4 = read4(self._buf4)
				if self._n4:
					self._i4 = 0
				else:
					break
		return i


obj = ReadContent()
global fileContent
fileContent="Read my Content"
buf = ['' for i in range(100)]
print(buf[:obj.read(buf,3)])
print(buf[:obj.read(buf,3)])
