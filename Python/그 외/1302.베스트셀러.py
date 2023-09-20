import sys
from collections import Counter
input = sys.stdin.readline
print(sorted(
    Counter(
        [input().rstrip()
         for _ in range(int(input()))]).items(),
    key=lambda x: (-x[1], x[0]))[0][0])
