N, M = map(int,input().split())

arr = set()
for _ in range(N):
    arr.add(input())

count = 0
for _ in range(M):
    if input() in arr:
        count += 1
print(count)