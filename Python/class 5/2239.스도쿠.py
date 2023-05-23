board = []
blank_positions = []


def is_valid_move(i, row, col):
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3

    if (
        i in board[row] or
        i in [board[j][col] for j in range(9)] or
        i in [board[block_row + m // 3][block_col + m % 3] for m in range(9)]
    ):
        return False
    return True


def backtracking(current_position, total_blanks):
    for i in range(1, 10):
        num = blank_positions[current_position]
        row = num // 10
        col = num % 10

        if is_valid_move(i, row, col):
            board[row][col] = i

            if current_position == total_blanks - 1 or backtracking(current_position + 1, total_blanks):
                return True

            board[row][col] = 0

    return False


board = [[int(j) for j in input()] for _ in range(9)]
blank_positions = [
    i * 10 + j for i, row in enumerate(board) for j, cell in enumerate(row) if cell == 0]

if backtracking(0, len(blank_positions)):
    for row in board:
        print(''.join(map(str, row)))
