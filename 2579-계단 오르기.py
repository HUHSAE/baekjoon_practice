
n = int(input())

stair = []
check = [0]*n

for i in range(n):
    stair.append(int(input()))
    
if len(stair) <= 2:
    print(sum(stair))
else:
    check[0] = stair[0]
    check[1] = stair[0] + stair[1]
    for i in range(2, n):
        check[i] = max(check[i-3] + stair[i-1] + stair[i], check[i-2] + stair[i])
        
    print(check[n-1])
    
