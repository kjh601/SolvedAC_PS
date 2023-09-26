import sys

N, M = map(int, sys.stdin.readline().split())
count_num = [0]*M

prev = 0
for now in map(int, sys.stdin.readline().split()):
    prev = (prev+now) % M
    count_num[prev] += 1

result = count_num[0]
for num in count_num:
    result += num*(num-1)//2
print(result)
