#큐는 First in First Out
import sys

queue = []

#시간초과 방지를 위해 input 말고 아래의 것을 사용
number = int(sys.stdin.readline())

for i in range(0, number):
    order = sys.stdin.readline().split()
    if(order[0])=="push":
        queue.append(int(order[1]))
    elif(order[0])=="pop":
        if(len(queue))==0:
            print("-1")
        else:
            print(queue.pop(0))
    elif(order[0])=="size":
        print(len(queue))
    elif(order[0])=="empty":
        if(len(queue))==0:
            print("1")
        else:
            print("0")
    elif(order[0])=="front":
        if(len(queue))==0:
            print("-1")
        else:
            print(queue[0])
    elif(order[0])=="back":
        if(len(queue))==0:
            print("-1")
        else:
            print(queue[-1])