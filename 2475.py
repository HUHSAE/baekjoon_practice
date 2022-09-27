

case = list(map(int, input().split()))

checknum = 0

for i in range (0, len(case)):
    checknum += case[i] * case[i]
    
checknum = checknum % 10

print(checknum)