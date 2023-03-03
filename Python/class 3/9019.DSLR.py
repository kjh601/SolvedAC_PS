from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write


def D(num):
    return (num*2) % 10000


def S(num):
    return (num-1) % 10000


def L(num):
    return (num//1000)+(num % 1000)*10


def R(num):
    return (num % 10)*1000+(num//10)


def bfs(start, end):
    queue = deque([start])
    link[start] = -1
    while True:
        output = queue.popleft()
        if output == end:
            return output
        else:
            num = D(output)
            if not num in link:
                queue.append(num)
                link[num] = (output, 'D')
            num = S(output)
            if not num in link:
                queue.append(num)
                link[num] = (output, 'S')
            num = L(output)
            if not num in link:
                queue.append(num)
                link[num] = (output, 'L')
            num = R(output)
            if not num in link:
                queue.append(num)
                link[num] = (output, 'R')


T = int(input())
for _ in range(T):
    st, ed = map(int, input().split())
    link = dict()
    route = []
    bfs(st, ed)
    curr = ed
    link.pop(st)
    while curr in link:
        route.append(link[curr][1])
        curr = link[curr][0]
    for cmd in reversed(route):
        output(cmd)
    output('\n')
