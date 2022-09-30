import sys

n = int(sys.stdin.readline())

#우측정렬을 해서 출력하기 위해 rjust사용
for i in range(0, n):
    submit = "*"*(i+1)
    print(submit.rjust(n))