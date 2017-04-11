"""
:Author: Pravallika
:Platform: Cracking the coding interview
:Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""

def arrayLeftRotate(list,n,k):
	#list = list of elements
	#n = size of the list
	#k = number of rotations
	
	for i in range(k):
		list.append(list.pop(0))
	print(list)

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
arrayLeftRotate(a,n,k)

