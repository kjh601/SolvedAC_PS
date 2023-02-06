from collections import Counter
import sys
input = sys.stdin.readline

def get_time(level, block_num):
    count = 0
    for height,num in arr.items():
        if height > level:
            count += (height-level)*num*2
            block_num += (height-level)*num
        if height < level:
            count += (level-height)*num
            block_num -= (level-height)*num
    if block_num < 0:
        return -1
    return count
N,M,B = map(int,input().split())
arr = Counter(sum([list(map(int,input().split())) for _ in range(N)],[]))
min_time = 64000000

for level in range(256, -1, -1):
    time = get_time(level,B)
    if time < 0 :
        continue
    if time < min_time:
        min_time = time
        floor = level
print(min_time, floor)