from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

queue = deque([1])
visited = [False] * 101
visited[1] = True
dist = [0] * 101

while queue:
    curr = queue.popleft()

    for i in range(1, 7):
        next = curr + i

        if next > 100:
            continue

        if next in ladder:
            next = ladder[next]

        if next in snake:
            next = snake[next]

        if not visited[next]:
            visited[next] = True
            dist[next] = dist[curr] + 1
            queue.append(next)

print(dist[100])