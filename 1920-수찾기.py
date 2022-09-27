#이진탐색(Binary Search) 사용
#이진탐색은 반드시 sort된 이후에 시작해야함
#시간복잡도는 log n
#배열 전체의 중간값을 찾으려하는 target 값과 비교,
#중간값이 target보다 큰경우에는 왼쪽을 선택, 아닐 경우엔 오른쪽을 선택
#선택한 부분의 중간값과 target값을 다시 비교
import sys

n = int(sys.stdin.readline())

an  = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

mlist = list(map(int, sys.stdin.readline().split())) 

an.sort()

#조건문 조건 주의
for i in mlist:
    isempty = False
    left = 0
    right =  n - 1
    while left <= right:
        mid = (left + right)//2
        if an[mid] == i:
            isempty = True
            print(1)
            break
        elif i < an[mid]:
            right = mid - 1
        elif i > an[mid]:
            left = mid + 1
    
    if  isempty ==  False:
        print(0)
        
