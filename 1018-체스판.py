import sys

n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())
 
 #아래 반복문은 전체 체스판을 8*8 체스판으로 바꾸기 위해 잡을 수 있는 시작점들을 찾기위한 반복문
for i in range(n-7):
    for j in range(m-7):
        #여기서 white는 시작점이 w로 시작될 경우 체스 판의 갯수를 세기 위함이고
        #black은 시작점이 b로 시작될 경우 체스 판의 갯수를 세기 위함이다.
        white = 0
        black = 0
 
        #위에서 찾은 시작점들을 기준으로 8칸씩 체크
        for a in range(i, i+8):
            for b in range(j, j+8):
                #현재 행과 열의 번호인 a와 b의 합이 짝수이면 시작점의 색과 같아야하고, 홀수이면 달라야한다.
                #먼저 합이 짝수인 경우 체크
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        white += 1
                    if board[a][b] != 'W':
                        black += 1
                #그다음 홀수인 경우 체크
                else:
                    if board[a][b] != 'W':
                        white += 1
                    if board[a][b] != 'B':
                        black += 1
 
        result.append(min(white, black))
 
print(min(result))