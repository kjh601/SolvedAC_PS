from sys import stdin
input = stdin.readline

move = {
    "R" : (0,1),
    "L" : (0,-1),
    "B" : (-1,0),
    "T" : (1,0),
    "RT" : (1,1),
    "LT" : (1,-1),
    "RB" : (-1,1),
    "LB" : (-1,-1)
}

king, dol, N = input().split()

dol_x = int(dol[1])-1
dol_y = ord(dol[0])-ord('A')

cur_x = int(king[1])-1
cur_y = ord(king[0])-ord('A')

N = int(N)
for _ in range(N):
    cmd = input().strip()
    nxt_x = cur_x + move[cmd][0]
    nxt_y = cur_y + move[cmd][1]
    if not ((0 <= nxt_x < 8) and (0<= nxt_y < 8)):
        continue
    if nxt_x == dol_x and nxt_y == dol_y:
        nxt_dol_x = dol_x + move[cmd][0]
        nxt_dol_y = dol_y + move[cmd][1]
        if not ((0 <= nxt_dol_x < 8) and (0<= nxt_dol_y < 8)):
            continue
        dol_x, dol_y = nxt_dol_x, nxt_dol_y
    cur_x, cur_y = nxt_x, nxt_y
    
print(chr(cur_y+ord('A'))+str(cur_x+1))
print(chr(dol_y+ord('A'))+str(dol_x+1))