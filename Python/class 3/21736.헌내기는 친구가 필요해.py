import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input())for _ in range(N)]


def dfs(start):
    stack = [start]
    count = 0
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        x, y = stack.pop()
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if 0 <= X < N and 0 <= Y < M and board[X][Y] != 'X':
                stack.append((X, Y))
                if board[X][Y] == 'P':
                    count += 1
                board[X][Y] = 'X'
    return count


for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            start = (i, j)
            break

result = dfs(start)
if result:
    print(result)
else:
    print('TT')
