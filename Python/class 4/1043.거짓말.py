from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a, *arr = map(int, input().split())
truth_knowers = set(arr)

linked_list = {i: set() for i in range(1, N+1)}


def spread_truth():
    stack = deque(truth_knowers)

    while stack:
        output = stack.pop()
        for node in linked_list[output]:
            if node in truth_knowers:
                continue
            truth_knowers.add(node)
            stack.append(node)


parties = [list(map(int, input().split()))for _ in range(M)]

for _, *party in parties:
    for p1 in party:
        for p2 in party:
            if p1 == p2:
                continue
            linked_list[p1].add(p2)
            linked_list[p2].add(p1)

spread_truth()

count = M
for _, *party in parties:
    for p in party:
        if p in truth_knowers:
            count -= 1
            break
# print(truth_knowers)
print(count)
