from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(st, linked_list: dict):
    dists = [INF for _ in range(N+1)]
    dists[st] = 0
    queue = [(0, st)]

    while queue:
        curr_w, curr_v = heappop(queue)
        for nxt_w, nxt_v in linked_list[curr_v]:
            dist = curr_w + nxt_w
            if dist >= dists[nxt_v]:
                continue
            dists[nxt_v] = dist
            heappush(queue, (dist, nxt_v))
    return dists[1:]


N, M, X = map(int, input().split())

path_to_X = {i: set() for i in range(1, N+1)}
path_from_X = {i: set() for i in range(1, N+1)}

for _ in range(M):
    x, y, w = map(int, input().split())

    path_to_X[y].add((w, x))
    path_from_X[x].add((w, y))

print(max(a + b for a, b in zip(dijkstra(X, path_to_X),
                                dijkstra(X, path_from_X))))
