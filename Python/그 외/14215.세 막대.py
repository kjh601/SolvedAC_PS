a = list(map(int, input().split()))
a.sort()
if a[0] + a[1] > a[2]:
    print(a[0] + a[1] + a[2])
else:
    print((a[0] + a[1]) * 2 - 1)
