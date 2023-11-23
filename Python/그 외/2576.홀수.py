import sys
input = sys.stdin.readline

sum_num = 0
min_num = 100

for _ in range(7):
    num = int(input())
    if num % 2 == 0:
        continue
    sum_num += num
    min_num = min(min_num, num)

if sum_num:
    print(sum_num, min_num, sep="\n")
else:
    print(-1)
