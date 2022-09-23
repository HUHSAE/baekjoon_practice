import sys


#시간초과 방지를 위해 input 말고 아래의 것을 사용
number = int(sys.stdin.readline())

for i in range(0, number):
    check = 0
    stack = list(sys.stdin.readline().strip())
    l = len(stack)
    for j in range(0, l):
        if(len(stack)==0):
                break
        else:
            last = stack.pop()
            if(last == ")"):
                check += 1
            elif(last == "("):
                if(check == 0):
                    check -= 1
                    break
                check -= 1
    if(check == 0):
        print("YES")
    else:
        print("NO")
