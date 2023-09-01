import sys
input = sys.stdin.readline


def dist(a, b):
    count = 0
    for i in range(4):
        count += int(a[i] != b[i])
    return count


def calculate_dist(a, b, c):
    return dist(a, b)+dist(b, c)+dist(c, a)


def choose_three_mbtis(arr):
    n = len(arr)
    min_dist = 12
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                min_dist = min(min_dist, calculate_dist(
                    arr[i], arr[j], arr[k]))
    return min_dist


for _ in range(int(input())):
    N = int(input())
    mbtis = input().split()
    if N > 32:
        print(0)
        continue
    print(choose_three_mbtis(mbtis))
