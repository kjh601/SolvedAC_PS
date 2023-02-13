from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    visited = set()
    stack = deque([start])
    while stack:
        output = stack.pop()
        if output in visited:
            continue
        print(output, end=' ')
        visited.add(output)
        stack.extend(matrix[output])
    print()

def BFS(start):
    visited = set()
    queue = deque([start])
    while queue:
        output = queue.popleft()
        if output in visited:
            continue
        print(output, end=' ')
        visited.add(output)
        queue.extend(matrix[output])
    print()    

N, M, V = map(int,input().split())

matrix = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int,input().split())
    matrix[node1].append(node2)
    matrix[node2].append(node1)

for i in range(N+1):
    matrix[i].sort(reverse=True)
DFS(V)

for i in range(N+1):
    matrix[i].sort()
BFS(V)
