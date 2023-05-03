import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
print(' '.join(map(str, arr[1:])))
