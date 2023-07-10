from collections import defaultdict
from sys import stdin
input = stdin.readline

T = int(input())

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

count = 0
A_dict = defaultdict(int)
for s in range(N):
    for e in range(s, N):
        A_dict[sum(A[s:e + 1])] += 1

for s in range(M):
    for e in range(s, M):
        count += A_dict[ T - sum(B[s:e + 1])]
        
print(count)
