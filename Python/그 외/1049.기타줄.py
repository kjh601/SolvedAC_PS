import sys
input = sys.stdin.readline

N, M = map(int, input().split())

min_package = 1000
min_each = 1000

for _ in range(M):
    package, each = map(int, input().split())
    min_package = min(min_package, package)
    min_each = min(min_each, each)

print(min(min_package, min_each*6)*(N//6)+min(min_package, min_each*(N % 6)))
