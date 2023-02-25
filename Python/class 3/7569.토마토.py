from collections import deque
import sys
input = sys.stdin.readline

def print_matrix():
    print()
    for i in range(H):
        print(i)
        for j in range(N):
            print(matrix[i][j])

def find_unripe_linked_to_ripe(loc):
    riped = deque([loc])
    unriped = []
    delta = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
    while riped :
        x, y, z = riped.popleft()
        for delta_x, delta_y, delta_z in delta:
            X = x+delta_x
            Y = y+delta_y
            Z = z+delta_z
            if 0>X or X>=H or 0>Y or Y>=N or 0>Z or Z>=M:
                continue
            elif  matrix[X][Y][Z] == -1:
                continue
            elif matrix[X][Y][Z] == 1:
                riped.append((X,Y,Z))
                matrix[X][Y][Z] = -1
            else:
                unriped.append((X,Y,Z))
                matrix[X][Y][Z] = -1
    return unriped


def bfs(arr):
    stack1 = deque(arr)
    stack2 = deque()
    count = 0
    delta = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
    while stack1:
        x, y, z = stack1.popleft()
        for delta_x, delta_y, delta_z in delta:
            X = x+delta_x
            Y = y+delta_y
            Z = z+delta_z
            if 0>X or X>=H or 0>Y or Y>=N or 0>Z or Z>=M:
                continue
            elif  matrix[X][Y][Z] == 0:
                stack2.append((X,Y,Z))
                matrix[X][Y][Z] = -1
        if not stack1:
            stack1.extend(stack2)
            stack2.clear()
            count += 1

    return count

def check_unriped_tomatoes():
    for floor in matrix:
        for line in floor:
            if 0 in line:
                return True
    return False

M, N, H = map(int,input().split())

matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

unripe_linked_to_ripe = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                matrix[i][j][k] = -1
                unripe_linked_to_ripe.extend(find_unripe_linked_to_ripe((i,j,k)))

count = bfs(unripe_linked_to_ripe)

if check_unriped_tomatoes():
    print(-1)
else :
    print(count)
