import sys

an  = sys.stdin.readline().strip()
line = list(an)
check = [0]*26
num = 0

for i in range(0, len(line)):
    if ord(line[i]) >= 97:
        num = ord(line[i]) - 97
        check[num] += 1
    elif ord(line[i]) <= 90:
        num = ord(line[i]) - 65
        check[num] += 1

#중복값 체크하기위해서 count 함수 사용
if check.count(max(check)) >= 2:
    print("?")
else:
    print(chr(check.index(max(check))+65))




#abcdef...배열 만들어서 안에 카운트        
        
    