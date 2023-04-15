import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp_ho = [[0 for _ in range(N)] for _ in range(N)]
dp_ve = [[0 for _ in range(N)] for _ in range(N)]
dp_di = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    if board[0][i] == 1:
        break
    dp_ho[0][i] = 1

for i in range(1, N):
    for j in range(1, N):
        if board[i][j] == 1:
            continue
        dp_ho[i][j] = dp_ho[i][j-1] + dp_di[i][j-1]
        dp_ve[i][j] = dp_ve[i-1][j] + dp_di[i-1][j]
        if not (board[i][j-1] == 1 or board[i-1][j] == 1):
            dp_di[i][j] = dp_ho[i-1][j-1] + dp_ve[i-1][j-1] + dp_di[i-1][j-1]

print(dp_ho[N-1][N-1]+dp_ve[N-1][N-1]+dp_di[N-1][N-1])
