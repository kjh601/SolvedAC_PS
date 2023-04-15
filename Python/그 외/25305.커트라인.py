N, k = map(int, input().split())
arr = list(map(int, input().split()))

print(sorted(arr, reverse=True)[k-1])
