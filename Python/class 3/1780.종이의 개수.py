from collections import deque
import sys
input = sys.stdin.readline

def check_paper(row,col,L):
    num = matrix[row][col]
    for i in range(row,L+row):
        for j in range(col,L+col):
            if num != matrix[i][j]:
                return 2
    return num

def bfs(row, col, L):
    stack = deque([(row, col, L)])
    while stack:
        node = stack.pop()
        num = check_paper(*node)
        if num!=2:
            count[num] += 1
        else :
            row,col,L = node
            cals = [
                (row,col,L//3), (row,col+L//3,L//3), (row,col+2*L//3,L//3), 
                (row+L//3,col,L//3), (row+L//3,col+L//3,L//3), (row+L//3,col+2*L//3,L//3), 
                (row+2*L//3,col,L//3), (row+2*L//3,col+L//3,L//3), (row+2*L//3,col+2*L//3,L//3)
                ]
            stack.extend(cals)

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
count = [0,0,0]
bfs(0,0,N)

print(count[-1])
print(count[0])
print(count[1])