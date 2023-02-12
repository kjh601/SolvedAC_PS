from collections import deque
import sys
input = sys.stdin.readline

def in_the_board(X,Y,N,M):
    return (0<=X<N)*(0<=Y<M)

def bfs(X,Y,N,M):
    queue = deque()
    queue.appendleft((X,Y))
    board[X][Y] = 0
    op = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        X,Y = queue.pop()
        for op_x,op_y in op:
            if not in_the_board(X+op_x,Y+op_y,N,M):
                continue
            if board[X+op_x][Y+op_y]:
                queue.appendleft((X+op_x,Y+op_y))
                board[X+op_x][Y+op_y] = 0

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    board = [[0]*M for _ in range(N)]

    for _ in range(K):
        Y,X = map(int, input().split())
        board[X][Y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                bfs(i,j,N,M)
                count += 1
    print(count)