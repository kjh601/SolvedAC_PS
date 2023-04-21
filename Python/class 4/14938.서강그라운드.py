from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(v):
    dists = [INF for _ in range(n+1)]
    dists[v] = 0
    queue = [(0, v)]
    while queue:
        curr_w, curr_v = heappop(queue)
        for nxt_w, nxt_v in linked_list[curr_v]:
            dist = curr_w+nxt_w
            if dist >= dists[nxt_v]:
                continue
            dists[nxt_v] = dist
            heappush(queue, (dist, nxt_v))
    return dists


n, m, r = map(int, input().split())

arr = [0]
arr.extend(list(map(int, input().split())))

linked_list = {i: [] for i in range(1, n+1)}
for _ in range(r):
    v1, v2, w = map(int, input().split())
    linked_list[v1].append((w, v2))
    linked_list[v2].append((w, v1))

max_item = 0
for start_v in range(1, n+1):
    count_item = 0
    for i, dist in enumerate(dijkstra(start_v)[1:], 1):
        if m < dist:
            continue
        count_item += arr[i]
    max_item = max(max_item, count_item)

print(max_item)
