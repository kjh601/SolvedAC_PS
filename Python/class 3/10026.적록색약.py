from collections import deque
import sys
input = sys.stdin.readline

def compare_color(is_color_weakness, color1, color2):
    if is_color_weakness and (color1 == 'R' or color1 == 'G') :
        if color2 == 'R' or color2 == 'G':
            return True
    elif color1 == color2:
        return True
    else:
        return False
        

def bfs(is_color_weakness, loc, color):
    queue = deque([loc])
    delta = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        x, y = queue.pop()
        for delta_x, delta_y in delta:
            X = x + delta_x
            Y = y + delta_y
            if 0 > X or X >= N or 0 > Y or Y >= N:
                continue
            if visited[is_color_weakness][X][Y]:
                continue
            if compare_color(is_color_weakness, matrix[X][Y], color):
                queue.append((X,Y))
                visited[is_color_weakness][X][Y] = True


N = int(input())
visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]
matrix = [input().rstrip() for _ in range(N)]

count = [0,0]
for i in range(N):
    for j in range(N):
        for is_color_weakeness in [False, True]:
            if not visited[is_color_weakeness][i][j]:
                bfs(is_color_weakeness, (i,j), matrix[i][j])
                count[is_color_weakeness] += 1

for num in count:
    print(num, end=' ')
