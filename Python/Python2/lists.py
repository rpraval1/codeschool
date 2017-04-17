"""
:Author: Pravallika
:Description: All possible operations on a List
"""

if __name__ == '__main__':
    N = int(raw_input())
    num_list = []
    for var in range(1,N+1):
        command = raw_input()
        #print(command)
        c_list = command.split(' ')
        #print(c_list)
        if (c_list[0] == 'insert'):
            num_list.insert(int(c_list[1]),int(c_list[2]))
            #print(num_list)
        if (c_list[0] == 'print'):
            print(num_list)
        if (c_list[0] == 'remove'):
            num_list.remove(int(c_list[1]))
        if (c_list[0] == 'append'):
            num_list.append(int(c_list[1]))
        if (c_list[0] == 'sort'):
            num_list.sort()
        if (c_list[0] == 'pop'):
            num_list.pop()
        if (c_list[0] == 'reverse'):
            num_list.reverse()
            
