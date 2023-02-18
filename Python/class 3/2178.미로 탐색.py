import sys
input = sys.stdin.readline

def bfs(start):
    nodes = [start]
    count = 1
    while board[N-1][M-1] == '1':
        tmp = []
        cals = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count+=1
        for row, col in nodes:
            for cal in cals:
                cal_row = row + cal[0]
                cal_col = col + cal[1]
                if 0 <= cal_row < N and 0 <= cal_col < M and board[cal_row][cal_col] == '1':
                    board[cal_row][cal_col] = '0'
                    tmp.append((cal_row, cal_col))
        nodes = tmp
    return count

N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
print(bfs((0,0)))
