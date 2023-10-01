from collections import defaultdict, deque
import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
A = list(map(int,input().split()))
sorted_A = sorted(A)
orders = defaultdict(deque)

idx = 0
for num in sorted_A:
    orders[num].append(idx)
    idx += 1
    
for num in A:
    write(str(orders[num].popleft())+' ')