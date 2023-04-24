import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
v = int(input())

count = 0
for num in arr:
    if num == v:
        count += 1
print(count)
