import sys
input = sys.stdin.readline
write = sys.stdout.write
def painted_one_color(row,col,length):
    color = board[row][col]
    for i in range(row,row+length):
        for j in range(col,col+length):
            if color != board[i][j]:
                return -1
    return color

def dfs(start):
    stack = [start]
    length = 0
    while stack:
        node = stack.pop()
        if node == '(' or node == ')':
            write(node)
            continue
        result = painted_one_color(*node)
        if result != -1:
            write(result)
        else :
            length = node[2]
            stack.extend([')',
                        (node[0]+node[2]//2,node[1]+node[2]//2,node[2]//2),
                        (node[0]+node[2]//2,node[1],node[2]//2),
                        (node[0],node[1]+node[2]//2,node[2]//2),
                        (node[0],node[1],node[2]//2),'('
                        ])

N = int(input())
board = [input().rstrip() for _ in range(N)]
dfs((0,0,N))
