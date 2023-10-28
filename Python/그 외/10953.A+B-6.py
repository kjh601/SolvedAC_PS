import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
for _ in range(N):
    a, b = map(int, input().split(','))
    write(str(a+b)+'\n')
