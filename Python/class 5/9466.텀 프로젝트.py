import sys
input = sys.stdin.readline


for _ in range(int(input())):
    count = 0

    n = int(input())
    arr = [0]+list(map(int,input().split()))
    visited = [False] * (n+1)
    stack = []

    for i in range(1,n+1):
        if visited[i]:
            continue

        idx = i
        while not visited[idx]:
            stack.append(idx)
            visited[idx] = True
            idx = arr[idx]
        
        pop_count = 0
        while True:
            pop_count += 1
            if idx == stack.pop():
                break
            if not stack:
                count += pop_count
                break
        count += len(stack)
        stack = []

    print(count)     