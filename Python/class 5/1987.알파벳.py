import sys
input = sys.stdin.readline

visited = [False]*26
deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def backtracking(x, y, length):
    max_length = length
    for delta_x, delta_y in deltas:
        X = x + delta_x
        Y = y + delta_y
        if not (0 <= X < R and 0 <= Y < C):
            continue
        if visited[ord(board[X][Y])-65]:
            continue
        visited[ord(board[X][Y])-65] = True
        max_length = max(max_length, backtracking(X, Y, length+1))
        visited[ord(board[X][Y])-65] = False
    return max_length


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
visited[ord(board[0][0])-65] = True
print(backtracking(0, 0, 1))
