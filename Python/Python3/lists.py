"""
:Author: Pravallika
:Description: All possible operations on a List
"""

if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        command = input()
        cList = command.split(" ")
        if cList[0]=='insert':
            myList.insert(int(cList[1]), int(cList[2]))
        if cList[0]=='print':
            print(myList)
        if cList[0]=='remove':
            myList.remove(int(cList[1]))
        if cList[0]=='append':
            myList.append(int(cList[1]))
        if cList[0]=='sort':
            myList.sort()
        if cList[0]=='pop':
            myList.pop()
        if cList[0]=='reverse':
            myList.reverse()
