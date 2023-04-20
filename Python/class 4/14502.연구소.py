from collections import deque
import sys
input = sys.stdin.readline


def count_safe_zone():
    queue = deque(viruses)
    visited = set()
    count = 0
    while queue:
        x, y = queue.pop()
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if 0 > X or X >= N:
                continue
            if 0 > Y or Y >= M:
                continue
            if (X, Y) in visited:
                continue
            if board[X][Y] == '0':
                queue.appendleft((X, Y))
                visited.add((X, Y))
                count += 1
    return count_empty - count


def backtracking(st, depth):
    if depth == 3:
        return count_safe_zone()
    else:
        max_count = -99999
        for num in range(st, N*M):
            i = num // M
            j = num % M
            if board[i][j] != '0':
                continue
            board[i][j] = '1'
            max_count = max(max_count, backtracking(num+1, depth+1))
            board[i][j] = '0'
        return max_count


N, M = map(int, input().split())
board = [input().split() for _ in range(N)]

count_empty = -3
viruses = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            count_empty += 1
        elif board[i][j] == '2':
            viruses.append((i, j))

print(backtracking(0, 0))
