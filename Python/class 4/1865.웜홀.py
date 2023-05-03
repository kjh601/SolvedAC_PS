import sys
input = sys.stdin.readline
INF = sys.maxsize


def belman_ford():
    time = [INF for _ in range(N+1)]
    time[1] = 0

    for _ in range(N):
        flag = False
        for i in range(1, N+1):
            for j, cost in linked_list[i]:
                if time[j] > time[i] + cost:
                    flag = True
                    time[j] = time[i] + cost

        if not flag:
            return 'NO'
    return 'YES'


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    linked_list = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        linked_list[S].append((E, T))
        linked_list[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        linked_list[S].append((E, -T))

    print(belman_ford())
