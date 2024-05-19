from sys import stdin

def bfs():
    board = [list(map(int,input().split())) for _ in range(5)]
    r, c = map(int,input().split())

    now = [(r,c)]
    nxt = []
    count = 1
    visited = {now[0]}
    deltas = [(0,-1), (0,1), (1,0), (-1,0)]
    while now:
        x, y = now.pop()
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if not((0 <= X < 5) and (0 <= Y < 5)):
                continue
            if (X,Y) in visited:
                continue
            if board[X][Y] == -1:
                continue
            if board[X][Y] == 1:
                return count
            
            nxt.append((X,Y))
            visited.add((X,Y))
        if not now:
            now = nxt
            nxt = []
            count += 1
    return -1

print(bfs())