import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(' '.join(map(str, [bisect.bisect_right(B, A[i]) - 1 - i for i in range(N)])))
