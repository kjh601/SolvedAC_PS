from functools import cmp_to_key
from math import log10
from sys import stdin
input = stdin.readline

K, N = map(int,input().split())
max_arr = sorted([input().rstrip() for _ in range(K)], key=lambda x: int(x),reverse=True)
max_arr.extend([max_arr[0]]*(N-K))
print(''.join(sorted(max_arr, key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))))