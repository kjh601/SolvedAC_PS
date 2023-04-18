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

        if num == k:
            if min_depth == 0:
                min_depth = depth
                count += 1
            elif min_depth == depth:
                count += 1

        for x in [num-1, num+1, num*2]:
            if -1 < x < 100001 and x not in visited:
                nxt.append(x)

        if not curr:
            depth += 1
            curr, nxt = nxt, []

    return min_depth, count


n, k = map(int, input().split())
min_depth, count = bfs(n, k)
print(min_depth)
print(count)
