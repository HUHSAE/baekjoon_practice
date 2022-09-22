#덱은 양끝에서 삽입과 삭제가 가능하다
from collections import deque
#collections 모듈에 deque 클래스로 구현이 되어 있다
import sys

deck = deque()

number = int(sys.stdin.readline())

for i in range(0, number):
    order = sys.stdin.readline().split()
    if(order[0])=="push_front":
        deck.appendleft(int(order[1]))
    elif (order[0])=="push_back":
        deck.append(int(order[1]))
    elif (order[0]) =="pop_front":
        if len(deck)==0:
            print("-1")
        else:
            print(deck.popleft())
    elif (order[0]) =="pop_back":
        if len(deck)==0:
            print("-1")
        else:
            print(deck.pop())
    elif(order[0])=="size":
        print(len(deck))
    elif(order[0])=="empty":
        if(len(deck))==0:
            print("1")
        else:
            print("0")
    elif(order[0])=="front":
        if(len(deck))==0:
            print("-1")
        else:
            print(deck[0])
    elif(order[0])=="back":
        if(len(deck))==0:
            print("-1")
        else:
            print(deck[-1])


