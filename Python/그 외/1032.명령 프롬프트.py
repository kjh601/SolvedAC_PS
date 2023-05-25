N = int(input())
arr = list(input().rstrip())
for _ in range(N-1):
    idx = 0
    for ch in input().rstrip():
        if arr[idx] != ch:
            arr[idx] = '?'
        idx += 1

print(''.join(arr))
