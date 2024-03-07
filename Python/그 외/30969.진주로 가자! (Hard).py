N = int(input())

arr = [0] * 1001
cost = 0
count = 0
for i in range(N):
    d, c = input().split()
    c = int(c)
    if c > 1000:
        count += 1
    else:
        arr[c] += 1
    if d == "jinju":
        cost = c

for i in range(cost+1, 1001):
    count += arr[i]
print(cost)
print(count)