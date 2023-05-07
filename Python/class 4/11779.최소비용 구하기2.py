from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

linked_list = [dict() for i in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    if e in linked_list[s]:
        linked_list[s][e] = min(w, linked_list[s][e])
    else:
        linked_list[s][e] = w

start, end = map(int, input().split())

route = [None for _ in range(n+1)]


def dijkstra():
    dists = [INF for i in range(n+1)]
    dists[start] = 0
    queue = [(0, start)]
    while queue:
        curr_w, curr_v = heappop(queue)
        for nxt_v, nxt_w in linked_list[curr_v].items():
            dist = curr_w + nxt_w
            if dist < dists[nxt_v]:
                dists[nxt_v] = dist
                route[nxt_v] = curr_v
                heappush(queue, (dist, nxt_v))
    return dists[end]


print(dijkstra())
shortest_route = []
curr = end
while curr:
    shortest_route.append(curr)
    curr = route[curr]
print(len(shortest_route))
print(' '.join(map(str, shortest_route[::-1])))
