from collections import deque
import sys
input = sys.stdin.readline


tetrominos = [[[1, 1, 1, 1]],

              [[1, 1],
               [1, 1]],

              [[1, 0],
               [1, 0],
               [1, 1],],

              [[1, 0],
               [1, 1],
               [0, 1]],

              [[0, 1],
               [1, 1],
               [0, 1]]]


def I(row, col):
    result = 0
    if 0 <= col+3 < M:
        result = max(result, sum(board[row][col:col+4]))
    if 0 <= row+3 < N:
        result = max(result, board[row][col] + board[row+1][col]
                     + board[row+2][col] + board[row+3][col])

    return result


def O(row, col):
    result = 0
    if 0 <= row+1 < N and 0 <= col+1 < M:
        result = max(result, board[row][col] + board[row][col+1]
                     + board[row+1][col] + board[row+1][col+1])
    return result


def horizon(x, y, delta_x, delta_y, row, col, tetromino):
    sum = 0
    X = x
    Y = y
    for i in range(3):
        for j in range(2):
            sum += board[row+i][col+j]*tetromino[X][Y]
            Y += delta_y
        X += delta_x
        Y = y
    return sum


def vertical(x, y, delta_x, delta_y, row, col, tetromino):
    sum = 0
    X = x
    Y = y
    for i in range(2):
        for j in range(3):
            sum += board[row+i][col+j]*tetromino[X][Y]
            X += delta_x
        Y += delta_y
        X = x
    return sum


def LZT(row, col):
    result = 0
    values = [(0, 0, 1, 1), (0, 1, 1, -1), (2, 0, -1, 1), (2, 1, -1, -1)]
    for tetromino in tetrominos[2:]:
        if 0 <= row+2 < N and 0 <= col+1 < M:
            for value in values:
                result = max(horizon(*value, row, col, tetromino),
                             result)
        if 0 <= row+1 < N and 0 <= col+2 < M:
            for value in values:
                result = max(vertical(*value, row, col, tetromino),
                             result)

    return result


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, LZT(i, j))
        result = max(result, I(i, j))
        result = max(result, O(i, j))

print(result)
