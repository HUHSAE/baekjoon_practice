#이진탐색(Binary Search) 사용
#이진탐색은 반드시 sort된 이후에 시작해야함
#시간복잡도는 log n
#배열 전체의 중간값을 찾으려하는 target 값과 비교,
#중간값이 target보다 큰경우에는 왼쪽을 선택, 아닐 경우엔 오른쪽을 선택
#선택한 부분의 중간값과 target값을 다시 비교

#시간 초과 나서 파이썬 내장 라이브러리인 bisect 사용
#bisect_left는 입력한 리스트에서 해당 값을 삽입할 수 있는 가장 왼쪽 인덱스 (해당 값보다 작은 가장 큰수) 리턴
#bisect_right는 입력한 리스트에서 해당 값을 삽입할 수 있는 가장 오른쪽 인덱스 (해당 값보드 큰 가장 작은수) 리턴

from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline())

an  = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

mlist = list(map(int, sys.stdin.readline().split())) 

an.sort()

def count(list, left, right):
    right_index = bisect_right(list, right)
    left_index = bisect_left(list, left)
    return right_index - left_index

for i in range(len(mlist)):
    print(count(an, mlist[i], mlist[i]))



#시간초과 나서 수정
# #조건문 조건 주의
# for i in mlist:
#     an = backup.copy()
#     count = 0
#     left = 0
#     right =  n - 1
#     while left <= right:
#         mid = (left + right)//2
#         if an[mid] == i:
#             count += 1
            
#             right = right - 1
#         elif an[mid] > i:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     print(count)