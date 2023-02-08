import sys
input = sys.stdin.readline

N,M = map(int,input().split())

site = dict()
for _ in range(N):
    address, password = input().split()
    site[address] = password
for _ in range(M):
    print(site[input().rstrip()])
