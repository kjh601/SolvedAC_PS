import sys
input = sys.stdin.readline

def dfs(r,c):
    stack = [(r,c)]
    board[r][c] = '0'
    count = 0
    while stack:
        x,y = stack.pop()
        count += 1
        delta = [(-1,0),(1,0),(0,-1),(0,1)]
        for x_delta, y_delta in delta:
            X = x + x_delta
            Y = y + y_delta
            if 0 <= X < N and 0 <= Y < N and board[X][Y] == '1':
                board[X][Y] = '0'
                stack.append((X,Y))
    return count

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

complex_num = 0
house_nums = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            house_nums.append(dfs(i,j))
            complex_num += 1
print(complex_num)
for num in sorted(house_nums):
    print(num)
