a, b= map(int, input().split())

alist = []
blist = []

#숫자로 입력받은 세자리 수를 문자열로 바꾼후 각 자리를 따로 리스트에 집어넣음
for i in str(a):
    alist.append(i)
sub = alist[0]
alist[0] = alist[2]
alist[2] = sub

a = int(alist[0])*100 + int(alist[1])*10 + int(alist[2])
    
for i in str(b):
    blist.append(i)
    
sub = blist[0]
blist[0] = blist[2]
blist[2] = sub
    
b = int(blist[0])*100 + int(blist[1])*10 + int(blist[2])

if a>b:
    print(a)
else:
    print(b)
