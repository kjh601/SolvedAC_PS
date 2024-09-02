from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]
visited = [[2500]*n for _ in range(n)]

visited[0][0] = 0
queue = [(0,(0,0))]

deltas = [(1,0),(-1,0),(0,-1),(0,1)]

while queue:
    cur_cost, (cur_x, cur_y) = heappop(queue)
    for delta_x, delta_y in deltas:
        nxt_x = cur_x + delta_x
        nxt_y = cur_y + delta_y
        if not(0 <= nxt_x < n and 0 <= nxt_y < n):
            continue
        
        nxt_cost = cur_cost + (1-int(board[nxt_x][nxt_y]))
        if visited[nxt_x][nxt_y] <= nxt_cost:
            continue

        heappush(queue, (nxt_cost, (nxt_x, nxt_y)))
        visited[nxt_x][nxt_y] = nxt_cost

print(visited[n-1][n-1])
