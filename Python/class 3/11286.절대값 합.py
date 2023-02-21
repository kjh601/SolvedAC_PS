from heapq import heappop, heappush
import sys
input = sys.stdin.readline

abs_heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if abs_heap:
            print(heappop(abs_heap)[1])
        else :
            print(0)
    else :
        heappush(abs_heap, (abs(x),x))
