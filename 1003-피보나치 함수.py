#전역변수와 재귀함수를 사용했을 경우 시간초과가 발생해서
#아래와 같은 방법으로 해결
#아래의 두 리스트는 각 인덱스가 해당 숫자를 의미,
#각 인덱스 당 0과 1의 개수를 저장
zero = [1, 0]
one = [0, 1]
def fibonacci(n):
    #배열 안에 몇까지 0의 개수가 적혀있는지
    l = len(zero)
    #n이 배열 길이보다 클경우
    if n>=l:
        for i in range(l, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    #아니면 그냥 배열에서 찾아서 출력, 클경우엔 위에서 계산후 해당값 출력
    print(zero[n], one[n])
    
#테스트 케이스 개수를 입력받음
number = int(input())
case = []
        
#테스트 케이스들을 입력
for i in range(0, number):
    case.append(int(input()))
            
for i in range(0, number):
    fibonacci(case[i])
        