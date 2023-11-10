import sys
input = sys.stdin.readline

total = 0
max_total = 0
for _ in range(4):
    n,m = map(int,input().split())
    total += m-n
    max_total = max(max_total, total)
    
print(max_total)