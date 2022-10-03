from collections import deque

n, k = map(int, input().split())

que = deque()
check = 0
conlist = []
numk = 0

for i in range(0, n):
    que.append(i+1)
print('<', end='')
while que:
    check = que.popleft()
    numk += 1
    if numk != k:
        que.append(check)
    elif numk == k:
        print(check, end='')
        numk = 0
        if que: #que가 남아있다면
            print(',', end=' ')

print('>')

