N = int(input())

arr = []
cost = 0
for i in range(N):
    d, c = input().split()
    c = int(c)
    if d == "jinju":
        cost = c
    else:
        arr.append(c)
count = 0
for i in arr:
    if i > cost:
        count += 1
print(cost)
print(count)