from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([1])
    visited = set([1])
    while queue:
        output = queue.popleft()
        for node in matrix[output]:
            if node in visited:
                continue
            parents[node] = output
            queue.append(node)
            visited.add(node)


N = int(input())

matrix = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int,input().split())
    matrix[node1].append(node2)
    matrix[node2].append(node1)

parents = [0 for _ in range(N+1)]
bfs()

for i in range(2,N+1):
    sys.stdout.write(str(parents[i])+'\n')
    