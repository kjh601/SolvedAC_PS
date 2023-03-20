from heapq import heappush, heappop


def bfs(start, end):
    queue = [(0, start)]
    visited = {start}
    count = 0
    while queue:
        cost, curr_node = heappop(queue)
        visited.add(curr_node)
        if curr_node == end:
            return cost

        adjacent = curr_node-1
        if adjacent >= 0 and adjacent not in visited:
            heappush(queue, (cost+1, adjacent))
        adjacent = curr_node+1
        if adjacent < 100001 and adjacent not in visited:
            heappush(queue, (cost+1, adjacent))
        adjacent = curr_node*2
        if adjacent < 100001 and adjacent not in visited:
            heappush(queue, (cost, adjacent))

    return None


N, K = map(int, input().split())
print(bfs(N, K))
