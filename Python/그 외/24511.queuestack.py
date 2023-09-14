import sys
input = sys.stdin.readline

N = int(input())
queuestack = [j for i, j in zip(input().split(), input().split()) if i == '0']

M = int(input())
C = input().split()
C.reverse()
C.extend(queuestack)
C.reverse()
print(' '.join(C[:M]))
