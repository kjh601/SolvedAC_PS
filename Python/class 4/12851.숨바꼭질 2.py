def bfs(n, k):
    curr = [n]
    nxt = []
    visited = set()
    depth = 0
    count = 0
    min_depth = 0

    while curr:
        num = curr.pop()
        visited.add(num)

        if min_depth and min_depth == depth and num == k:
            count += 1
        if not min_depth and num == k:
            min_depth = depth
            count += 1

        if num > 0 and (num - 1) not in visited:
            nxt.append(num - 1)
        if num < 100000 and (num + 1) not in visited:
            nxt.append(num + 1)
        if num < 50001 and (num * 2) not in visited:
            nxt.append(num * 2)

        if not curr:
            depth += 1
            curr, nxt = nxt, []

    return min_depth, count


n, k = map(int, input().split())
min_depth, count = bfs(n, k)
print(min_depth)
print(count)
