import sys
input = sys.stdin.readline


def find_farthest_vertex(start):
    stack = [(0, start)]
    max_dist = 0
    farthest_v = start
    visited = [False for _ in range(V+1)]
    while stack:
        curr_w, curr_v = stack.pop()
        visited[curr_v] = True
        if curr_w > max_dist:
            max_dist = curr_w
            farthest_v = curr_v
        for nxt_w, nxt_v in linked_list[curr_v]:
            if visited[nxt_v]:
                continue
            stack.append((curr_w+nxt_w, nxt_v))
    return farthest_v, max_dist


def find_tree_diameter():
    return find_farthest_vertex(find_farthest_vertex(1)[0])[1]


V = int(input())

linked_list = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    s = arr[0]
    length = len(arr)-1
    for i in range(1, length, 2):
        e, w = arr[i], arr[i+1]
        linked_list[s].append((w, e))

print(find_tree_diameter())
