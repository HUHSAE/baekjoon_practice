#11399-ATM

num = int(input())

#테스트 케이스들을 입력
case = list(map(int, input().split()))

#파이썬의 sort함수로 리스트를 오름차순으로 정렬
case.sort()

l = len(case)
least = 0
total = 0

#들인 시간을 계산
for i in range (0, l):
    least += case[i]
    total += least
print(total)