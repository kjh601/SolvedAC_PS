from collections import deque
import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    N,K = map(int,input().split())
    buildingTime = [0]+list(map(int,input().split()))
    totalTime = [0]*(N+1)
    indegree = [0]*(N+1)
    linked_list = [[] for _ in range(N+1)]
    for _ in range(K):
        s,e = map(int,input().split())
        linked_list[s].append(e)
        indegree[e] += 1
    end = int(input())

    curr = 0
    queue = deque()
    visited = [False]*(N+1)
    while curr != end:
        idx = 1
        while idx < N+1:
            if not visited[idx] and indegree[idx] == 0:
                queue.appendleft(idx)
            idx += 1

        while queue:
            curr = queue.pop()
            totalTime[curr] += buildingTime[curr]
            visited[curr] = True
            for nxt in linked_list[curr]:
                totalTime[nxt] = max(totalTime[nxt], totalTime[curr])
                indegree[nxt] -= 1
        if queue:
            break
    result.append(totalTime[end])
print('\n'.join(map(str,result)))