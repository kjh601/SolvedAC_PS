from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra

N = int(input())
M = int(input())

graph
for _ in range(M):
    st, ed, cost = map(int,input().split())
