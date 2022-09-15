
number = input()

#공백을 기준으로 나눈 정수들을 한줄로 입력받음
numlist = map(int, input().split())
check = 0
for i in numlist:
    nonp = 0
    if i == 1:
        continue
    elif i == 2:
        check += 1
        continue
    for j in range(2,i):
        result = i % j
        if result == 0:
            nonp +=1
    if nonp == 0:
        check += 1

print(check)