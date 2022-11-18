import sys

case = [0 for i in range(11)]
case[1] = 1
case[2] = 2
case[3] = 4
case[4] = 7


T = int(input())

for i in range (5, 11):
    case[i] = case[i-1] + case[i-2] + case[i-3]


for i in range(0, T):
    number = int(input())
    print(case[number])

