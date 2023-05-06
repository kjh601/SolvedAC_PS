
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

walls = set()
for i in range(N):
    for j, is_wall in enumerate(input()):
        if is_wall == '1':
            walls.add((i, j))
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]


def bfs():
    curr = [(0, 0, False)]
    nxt = []
    count = 1
    while curr:
        x, y, break_wall = curr.pop()
        if x == N-1 and y == M-1:
            return count
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if not (0 <= X < N and 0 <= Y < M):
                continue
            if visited[X][Y][break_wall]:
                continue
            if (X, Y) in walls:
                if break_wall == 0:
                    nxt.append((X, Y, 1))
                    visited[X][Y][1] = 1
                continue
            nxt.append((X, Y, break_wall))
            visited[X][Y][break_wall] = 1
        if not curr:
            curr = nxt
            nxt = []
            count += 1
    return -1


print(bfs())
