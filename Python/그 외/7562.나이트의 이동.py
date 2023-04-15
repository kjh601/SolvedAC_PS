def bfs(row, col):
    now = [(row, col)]
    nxt = []
    count = 0
    visited = set()
    deltas = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
              (1, -2), (1, 2), (2, -1), (2, 1)]
    while now:
        x, y = now.pop()
        if x == ed_row and y == ed_col:
            return count
        for delta_x, delta_y in deltas:
            X = x+delta_x
            Y = y+delta_y
            if 0 <= X < l and 0 <= Y < l and (X, Y) not in visited:
                nxt.append((X, Y))
                visited.add((X, Y))
        if not now:
            count += 1
            now.extend(nxt)
            nxt = []


T = int(input())

for _ in range(T):
    l = int(input())
    st_row, st_col = map(int, input().split())
    ed_row, ed_col = map(int, input().split())

    print(bfs(st_row, st_col))
