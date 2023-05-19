N = int(input())
arr = list(map(int, input().split()))

idx1 = 0
idx2 = N-1
min_idx1 = idx1
min_idx2 = idx2
min_sum = 2000000000
while idx1 != idx2:
    S = arr[idx1] + arr[idx2]
    if abs(S) < min_sum:
        min_sum = abs(S)
        min_idx1 = idx1
        min_idx2 = idx2
    if S < 0:
        idx1 += 1
    elif S > 0:
        idx2 -= 1
    else:
        break
print(arr[min_idx1], arr[min_idx2])
