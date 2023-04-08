def print_triangle(x, y):
    board[x][y] = '*'
    board[x+1][y-1] = '*'
    board[x+1][y+1] = '*'
    for i in range(5):
        board[x+2][y-2 + i] = '*'


def recursion(x, y, num):
    if num == 3:
        print_triangle(x, y)
    else:
        num //= 2

        recursion(x, y, num)
        recursion(x+num, y-num, num)
        recursion(x+num, y+num, num)


N = int(input())
board = [[' 'for _ in range(5*(N//3)+N//3)]for _ in range(N+1)]
recursion(1, N, N)
for line in board[1:]:
    print(''.join(line[1:]))
