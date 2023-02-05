"""체스판 다시 칠하기"""

def create_correct_answer(start_color):
    """정답지를 생성한다."""
    answer_board = []
    lines = ['WBWBWBWB','BWBWBWBW']
    if start_color=='W':
        start = 0
    else :
        start = 1
    for line in range(8):
        answer_board.append(lines[(line+start)%2])
    return answer_board

def count_worng_tiles(row,col,board1, board2):
    """정답과 다른 칸의 수를 센다."""
    count = 0
    for i in range(8):
        for j in range(8):
            if board1[row+i][col+j] == board2[i][j]:
                count+=1
    return count

def retrieve_minimum_count(row,col,board, correct_answer) :
    """최소 수를 찾아 반환한다."""
    min_count = 64
    for i in range(row-7):
        for j in range(col-7):
            min_count = min(min_count,count_worng_tiles(i,j,board, correct_answer))
    return min_count

M,N = map(int, input().split())

board = list()
for i in range(M) :
    board.append(input())

correct_answer = create_correct_answer('W')
count1 = retrieve_minimum_count(M,N, board, correct_answer)

correct_answer = create_correct_answer('B')
count2 = retrieve_minimum_count(M,N, board, correct_answer)

print(min(count1,count2))
