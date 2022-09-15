number = input()

#공백을 기준으로 나눈 정수들을 한줄로 입력받음
numlist = map(int, input().split())
check = 0
for i in numlist:
    nonp = 0
    #1과 2가 입력될 경우 아래 코드로 확인
    if i == 1:
        continue
    elif i == 2:
        check += 1
        continue
    
    for j in range(2,i):
        result = i % j
        #값 i를 2부터 i보다 작은 수로 나누었을 때 나누어떨어질 경우 소수가 아니므로 nonp+=1
        if result == 0:
            nonp +=1
            #break를 추가함으로 속도 약간 향상
            break
        
    #nonp가 0이라면 소수라는 뜻이므로 check 값을 증가
    if nonp == 0:
        check += 1

print(check)