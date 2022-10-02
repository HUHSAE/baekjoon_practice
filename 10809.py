import sys

an = sys.stdin.readline().strip()


al = 'abcdefghijklmnopqrstuvwxyz'

#출력이후 한칸 띄우기 위해 end = ' '사용
for i in al:
    if i in an:
        print(an.index(i), end = ' ')
    else:
        print(-1, end = ' ')
        
#이외에도 배열을 [-1]*26해서 초기화한 후 아스키코드 이용해서 풀어도됨