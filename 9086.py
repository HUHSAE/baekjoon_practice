import sys


#시간초과 방지를 위해 input 말고 아래의 것을 사용
number = int(sys.stdin.readline())

for i in range(0, number):
    check = 0
    stack = list(sys.stdin.readline().strip())
    print('%s%s'%(stack[0],stack[-1]))