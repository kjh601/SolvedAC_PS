import sys
input = sys.stdin.readline


deltas = [(-1,0), (1,0), (0,-1), (0,1)]
def spread_dust():
    temp = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if board[x][y] >= 5:
                spread = board[x][y] // 5
                cnt = 0
                for dx, dy in deltas:
                    X = x + dx
                    Y = y + dy
                    if 0 <= X < R and 0 <= Y < C and board[X][Y] != -1:
                        temp[X][Y] += spread
                        cnt += 1
                board[x][y] -= spread * cnt
    for x in range(R):
        for y in range(C):
            board[x][y] += temp[x][y]

def operate_purifier(purifier_loc):
    for i in range(purifier_loc - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
    for i in range(purifier_loc):
        board[i][C - 1] = board[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[purifier_loc][i] = board[purifier_loc][i - 1]
    board[purifier_loc][1] = 0

    for i in range(purifier_loc + 2, R - 1):
        board[i][0] = board[i + 1][0]
    for i in range(C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for i in range(R - 1, purifier_loc + 1, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[purifier_loc + 1][i] = board[purifier_loc + 1][i - 1]
    board[purifier_loc + 1][1] = 0

R, C, T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]

for i in range(R) :
    if board[i][0] == -1:
        loc = i
        break  

for _ in range(T):
    spread_dust()
    operate_purifier(loc)

total_dust = sum(sum(line) for line in board) + 2
print(total_dust)