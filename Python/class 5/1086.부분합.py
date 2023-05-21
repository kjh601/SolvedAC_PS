n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end, subtotal, min_length = 0, 0, 0, 100001

while end < n:
    while subtotal < s and end < n:
        subtotal += arr[end]
        end += 1
    while subtotal >= s and start < n:
        min_length = min(min_length, end - start)
        subtotal -= arr[start]
        start += 1

print(0 if min_length == 100001 else min_length)
