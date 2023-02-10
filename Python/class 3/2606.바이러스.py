from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    is_visit = [0 for _ in range(N+1)]
    is_visit[1] = 1
    queue = deque([1])
    count = 0
    while queue:
        node = queue.pop()
        for num in graph[node]:
            if is_visit[num] == 0:
                queue.appendleft(num)
                is_visit[num] = 1
                count+=1
    return count

N = int(input())
graph = [[] for _ in range(N+1)]

M = int(input())
for _ in range(M):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(BFS())
