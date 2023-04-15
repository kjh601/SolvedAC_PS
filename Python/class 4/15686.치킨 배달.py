import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(N)]


def get_dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def get_chicken_dist(house):
    result = INF
    for chicken in selected_chickens:
        result = min(result, get_dist(house, chicken))
    return result


def get_chicken_city_dist():
    result = 0
    for house in houses:
        result += get_chicken_dist(house)
    return result


def backtracking(st, depth):
    if depth == M:
        return get_chicken_city_dist()
    else:
        result = INF
        for i, chicken in enumerate(chickens[st:], st):
            selected_chickens.append(chicken)
            result = min(result, backtracking(i+1, depth+1))
            selected_chickens.pop()
        return result


houses = []
chickens = []
selected_chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

print(backtracking(0, 0))
