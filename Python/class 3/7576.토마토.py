from collections import deque
import sys
input = sys.stdin.readline

def find_unripe_linked_to_ripe(loc):
    riped = deque([loc])
    unriped = []
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    while riped :
        y, z = riped.popleft()
        for delta_y, delta_z in delta:
            Y = y+delta_y
            Z = z+delta_z
            if 0>Y or Y>=N or 0>Z or Z>=M:
                continue
            elif  matrix[Y][Z] == -1:
                continue
            elif matrix[Y][Z] == 1:
                riped.append((Y,Z))
                matrix[Y][Z] = -1
            else:
                unriped.append((Y,Z))
                matrix[Y][Z] = -1
    return unriped


def bfs(arr):
    stack1 = deque(arr)
    stack2 = deque()
    count = 0
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    while stack1:
        y, z = stack1.popleft()
        for delta_y, delta_z in delta:
            Y = y+delta_y
            Z = z+delta_z
            if 0>Y or Y>=N or 0>Z or Z>=M:
                continue
            elif  matrix[Y][Z] == 0:
                stack2.append((Y,Z))
                matrix[Y][Z] = -1
        if not stack1:
            stack1.extend(stack2)
            stack2.clear()
            count += 1

    return count

def check_unriped_tomatoes():
    for line in matrix:
        if 0 in line:
            return True
    return False

M, N = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

unripe_linked_to_ripe = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            matrix[i][j] = -1
            unripe_linked_to_ripe.extend(find_unripe_linked_to_ripe((i,j)))

count = bfs(unripe_linked_to_ripe)

if check_unriped_tomatoes():
    print(-1)
else :
    print(count)
