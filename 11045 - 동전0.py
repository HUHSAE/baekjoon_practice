import sys

n, k = map(int, input().split())

coin = []
check = 0

for i in range(n):
    coin.append(int(input()))
    
for i in reversed(coin):
    if i > k :
        continue
    elif i <= k :
        count = 0
        count = k//i
        k -= i*count
        check += count
        if k == 0:
            break

print(check)