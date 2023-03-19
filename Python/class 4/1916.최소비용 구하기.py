from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(graph, start, end):
    dists = {node: INF for node in graph}
    dists[start] = 0
    queue = []
    heappush(queue, (dists[start], start))

    while queue:
        curr_dist, curr_node = heappop(queue)

        if dists[curr_node] < curr_dist:
            continue

        for adjacent, weight in graph[curr_node].items():
            dist = curr_dist + weight

            if dist < dists[adjacent]:
                dists[adjacent] = dist
                heappush(queue, (dist, adjacent))

    return dists[end]


N = int(input())
M = int(input())

graph = {i: {} for i in range(1, N+1)}
for _ in range(M):
    st, ed, cost = map(int, input().split())
    if ed in graph[st]:
        graph[st][ed] = min(cost, graph[st][ed])
    else:
        graph[st][ed] = cost

S, E = map(int, input().split())
print(dijkstra(graph, S, E))
