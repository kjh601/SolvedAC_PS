"""단어 정렬"""
import sys

N = int(input())
words = {sys.stdin.readline().rstrip() for i in range(N)}
words = list(words)
print('\n'.join(sorted(sorted(words), key = len)))