import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

total_price = 0
for _ in range(N):
    a, b = map(int, input().split())
    total_price += a*b

if total_price == X:
    print('Yes')
else:
    print('No')
