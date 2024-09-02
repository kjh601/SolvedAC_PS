import sys
input = sys.stdin.readline
write = sys.stdout.write


def processCell(x, y):
    global count
    cell = board[x][y]

    if cell == '*':
        return

    if cell.islower():
        key.add(cell)
        stack.append((x, y))
        stack.extend(door.get(cell.upper(), []))
    elif cell in '.$' or cell.lower() in key:
        if cell == '$':
            count += 1
        stack.append((x, y))
    else:
        door[cell].append((x, y))

    board[x][y] = '*'


result = []
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    key = set(input().rstrip())
    if '0' in key:
        key = set()
    door = {
        'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [],
        'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []
    }

    stack = []
    count = 0

    for i in range(N):
        processCell(i, 0)
        processCell(i, M-1)
    for i in range(M):
        processCell(0, i)
        processCell(N-1, i)

    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    while stack:
        x, y = stack.pop()
        for delta_x, delta_y in delta:
            X = x + delta_x
            Y = y + delta_y
            if not (0 <= X < N and 0 <= Y < M):
                continue
            if board[X][Y] == '*':
                continue
            processCell(X, Y)

    write(str(count)+"\n")
