from collections import deque
import sys
input = sys.stdin.readline


def search_fish(st, size):
    queue = deque([st])
    next = []
    dist = 1
    loc_X = N
    loc_Y = N
    visited = set()
    visited.add(st)
    flag = False
    while queue:
        x, y = queue.popleft()
        deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if not (0 <= X < N and 0 <= Y < N):
                continue
            if board[X][Y] != 0 and board[X][Y] < size and board[X][Y] != 9:
                flag = True
                loc_X, loc_Y = min((loc_X, loc_Y), (X, Y))
                visited.add((X, Y))
            elif board[X][Y] > size or (X, Y) in visited:
                continue
            else:
                next.append((X, Y))
                visited.add((X, Y))
        if not queue:
            if flag:
                board[st[0]][st[1]] = 0
                board[loc_X][loc_Y] = 9
                return (loc_X, loc_Y), dist
            queue.extend(next)
            next = []
            dist += 1
    return st, 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            curr = (i, j)

time = 0
size = 2
left = size
while True:
    next, dist = search_fish(curr, size)
    if dist:
        left -= 1
        time += dist
        curr = next
    else:
        break
    if left == 0:
        size += 1
        left = size
print(time)
