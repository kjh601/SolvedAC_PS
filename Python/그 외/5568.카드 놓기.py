from itertools import combinations, permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
card_comb = combinations([int(input()) for _ in range(n)], k)

unique = set()
for comb in card_comb:
    card_perm = permutations(comb, k)
    for perm in card_perm:
        number = int(''.join(map(str, perm)))
        unique.add(number)

print(len(unique))
