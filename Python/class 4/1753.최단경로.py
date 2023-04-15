from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(st):
    queue = [(0, st)]
    weights = [INF for _ in range(N+1)]
    weights[st] = 0
    while queue:
        cur_weight, cur_node = heappop(queue)
        for nxt_weight, nxt_node in linked_list[cur_node]:
            weight = cur_weight + nxt_weight
            if weight < weights[nxt_node]:
                weights[nxt_node] = weight
                heappush(queue, (weight, nxt_node))
    return weights


N, E = map(int, input().split())
K = int(input())

linked_list = {i: [] for i in range(1, N+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    linked_list[u].append((w, v))

for weight in dijkstra(K)[1:]:
    if INF <= weight:
        print('INF')
    else:
        print(weight)
