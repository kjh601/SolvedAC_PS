from heapq import heappop, heappush
from sys import stdin, stdout

input = stdin.readline
write = stdout.write

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
    
inf = float('inf')
even_costs = [inf]*(N+1)
odd_costs = [inf]*(N+1)

even_costs[1] = 0

queue = [(0,1)]
while queue:
    curr_cost, curr_node = heappop(queue)
    
    if curr_cost % 2:
        if odd_costs[curr_node] < curr_cost:
            continue
    else:
        if even_costs[curr_node] < curr_cost:
            continue
    
    for cost, nxt_node in graph[curr_node]:
        nxt_cost = curr_cost + cost
        
        is_odd = nxt_cost%2
        
        if is_odd:
            if nxt_cost < odd_costs[nxt_node]:
                odd_costs[nxt_node] = nxt_cost
                heappush(queue, (nxt_cost, nxt_node))    
        else:
            if nxt_cost < even_costs[nxt_node]:
                even_costs[nxt_node] = nxt_cost
                heappush(queue, (nxt_cost, nxt_node))

for i in range(1, N+1):
    odd_cost = odd_costs[i] if odd_costs[i] != inf else -1
    even_cost = even_costs[i] if even_costs[i] != inf else -1
    
    write("%d %d\n" %(odd_cost, even_cost))