import sys
input = sys.stdin.readline
print = sys.stdout.write

dp = [0]*100001

N = int(input())
arr = list(map(int, input().split()))

result = 0
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())

    print(str(result))
