import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = tuple(map(int, input().split()))

idx1, idx2, subtotal, min_length = 0, 0, 0, 100001

while idx2 < n:
    while subtotal < s and idx2 < n:
        subtotal += arr[idx2]
        idx2 += 1
    while subtotal >= s and idx1 < n:
        min_length = min(min_length, idx2 - idx1)
        subtotal -= arr[idx1]
        idx1 += 1

print(0 if min_length == 100001 else min_length)
