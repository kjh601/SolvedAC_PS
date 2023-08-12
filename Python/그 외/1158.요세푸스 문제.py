N, M = map(int,input().split())
arr = list( i for i in range(1, N+1))
M-=1
idx = 0
result = []
while arr:
    idx = (idx+M) % len(arr)
    result.append(arr.pop(idx))
print("<"+", ".join(map(str, result))+">")