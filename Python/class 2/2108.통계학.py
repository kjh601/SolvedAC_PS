import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(8001)]
for _ in range(N):
    arr[int(input())]+=1

sum = 0
mid = 4001
idx = 0
max_frequency = 0
max_value = -4000
flag = True
for i in range(-4000,4001):
    sum+=i*arr[i]
    if arr[i]==0:
        continue
    if idx <= N//2 < idx+arr[i]:
        mid = i
    if max_frequency<arr[i]:
        flag2 = True
        max_frequency = arr[i]
        mode = i
    elif flag2 and max_frequency==arr[i]:
        flag2 = False
        mode = i
    max_value = max(max_value, i)
    if flag and arr[i]:
        min_value = i
        flag = False
    idx += arr[i]
print(round(sum/N))
print(mid)
print(mode)
print(max_value-min_value)