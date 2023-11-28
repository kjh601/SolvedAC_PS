import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
length = min(N, M)

for width in range(length-1, -1, -1):
    for r in range(N-width):
        for c in range(M-width):
            if board[r][c] == board[r+width][c] == board[r][c+width] == board[r+width][c+width]:
                print((width+1)**2)
                exit(0)
