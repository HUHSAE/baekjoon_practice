import sys
from collections import deque

queue = deque()

#시간초과 방지를 위해 input 말고 아래의 것을 사용
number = int(sys.stdin.readline())

for i in range (0, number):
    queue.append(i+1)
    
while(len(queue)!=1):
    queue.popleft()
    last = queue.popleft()
    queue.append(last)

print(queue[0])