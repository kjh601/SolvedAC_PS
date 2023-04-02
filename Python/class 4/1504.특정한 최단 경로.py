from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


def daijkstra(st, ed):
    queue = [(0, st)]
    dists = [INF for _ in range(N+1)]
    dists[st] = 0

    while queue:
        cur_dist, cur_node = heappop(queue)

        if cur_dist > dists[cur_node]:
            continue

        for nxt_dist, nxt_node in linked_list[cur_node]:
            dist = cur_dist + nxt_dist
            if dist < dists[nxt_node]:
                dists[nxt_node] = dist
                heappush(queue, (dist, nxt_node))

    return dists[ed]


N, E = map(int, input().split())

linked_list = {i: set() for i in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    linked_list[a].add((c, b))
    linked_list[b].add((c, a))

v1, v2 = map(int, input().split())

min_dist = daijkstra(v1, v2) + min(daijkstra(1, v1) +
                                   daijkstra(v2, N), daijkstra(1, v2)+daijkstra(v1, N))

if INF <= min_dist:
    print(-1)
else:
    print(min_dist)
