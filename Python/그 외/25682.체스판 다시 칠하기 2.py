import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = ['0'*(M+1)]+['0'+input().rstrip() for _ in range(N)]

sums = [[0]*(M+1) for _ in range(N+1)]


def cal_sum(start_black):
    for i in range(1, N+1):
        is_black = start_black
        for j in range(1, M+1):
            sums[i][j] = (0 if is_black == (board[i][j] == 'B') else 1) + \
                sums[i][j-1]+sums[i-1][j]-sums[i-1][j-1]
            is_black = not is_black
        start_black = not start_black

    min_sum = 4000000
    for i in range(K, N+1):
        for j in range(K, M+1):
            min_sum = min(min_sum, sum_square(i, j))

    return min_sum


def sum_square(a, b):
    c = a-K
    d = b-K

    return sums[a][b] - sums[a][d] - sums[c][b] + sums[c][d]


print(min(cal_sum(True), cal_sum(False)))
