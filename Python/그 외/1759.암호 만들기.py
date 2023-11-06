from itertools import combinations
import sys

input = sys.stdin.readline
write = sys.stdout.write


def count_vowels(string):
    return sum(1 for char in string if char in 'aeiou')


def find_passwords(L, chars):
    for combination in combinations(sorted(chars), L):
        password = ''.join(combination)
        vowels = count_vowels(password)
        if vowels < 1 or L - vowels < 2:
            continue
        write(password+'\n')


L, C = map(int, input().split())
chars = input().split()

find_passwords(L, chars)
