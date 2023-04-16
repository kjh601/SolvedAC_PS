import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for Ai in A:
    Ai -= B
    count += 1
    if Ai <= 0:
        continue
    count += Ai//C
    if Ai % C != 0:
        count += 1
print(count)
