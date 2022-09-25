num, large = map(int, input().split())

case = list(map(int, input().split()))
small = []
for i in range(0, len(case)):
    if case[i]<large:
        small.append(case[i])

str_small = str(small)
str_small = str_small.replace(',', '')
str_small = str_small.replace('[', '')
str_small = str_small.replace(']', '')
print(str_small)