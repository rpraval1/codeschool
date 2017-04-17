"""
:Author: Pravallika
:Description: Basic method to create a hash of a tuple(m,n).
                hash() is one of the functions of the __builtins__ module
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

