from collections import deque

lines = iter(open(0).read().split('\n'))
get_input = lines.__next__

m, n, o, p, q, r, s, t, u, v, w = map(int, get_input().split())

board = [[[[[[[[[[list(map(int, get_input().split())) for _ in range(n)]for _ in range(o)]for _ in range(p)]for _ in range(q)]
              for _ in range(r)]for _ in range(s)]for _ in range(t)]for _ in range(u)]for _ in range(v)]for _ in range(w)]

delta_w = [1, -1] + [0]*20
delta_v = [0]*2 + [1, -1] + [0]*18
delta_u = [0]*4 + [1, -1] + [0]*16
delta_t = [0]*6 + [1, -1] + [0]*14
delta_s = [0]*8 + [1, -1] + [0]*12
delta_r = [0]*10 + [1, -1] + [0]*10
delta_q = [0]*12 + [1, -1] + [0]*8
delta_p = [0]*14 + [1, -1] + [0]*6
delta_o = [0]*16 + [1, -1] + [0]*4
delta_n = [0]*18 + [1, -1] + [0]*2
delta_m = [0]*20 + [1, -1]

count = 0
zero_count = 0
cur = deque()
for w1 in range(w):
    for v1 in range(v):
        for u1 in range(u):
            for t1 in range(t):
                for s1 in range(s):
                    for r1 in range(r):
                        for q1 in range(q):
                            for p1 in range(p):
                                for o1 in range(o):
                                    for n1 in range(n):
                                        for m1 in range(m):
                                            if board[w1][v1][u1][t1][s1][r1][q1][p1][o1][n1][m1] == 1:
                                                cur.append(
                                                    (w1, v1, u1, t1, s1, r1, q1, p1, o1, n1, m1))
                                            elif board[w1][v1][u1][t1][s1][r1][q1][p1][o1][n1][m1] == 0:
                                                zero_count += 1
nxt = deque()
while cur:
    w1, v1, u1, t1, s1, r1, q1, p1, o1, n1, m1 = cur.pop()
    for i in range(22):
        W = w1 + delta_w[i]
        V = v1 + delta_v[i]
        U = u1 + delta_u[i]
        T = t1 + delta_t[i]
        S = s1 + delta_s[i]
        R = r1 + delta_r[i]
        Q = q1 + delta_q[i]
        P = p1 + delta_p[i]
        O = o1 + delta_o[i]
        N = n1 + delta_n[i]
        M = m1 + delta_m[i]
        if W < 0 or W >= w:
            continue
        if V < 0 or V >= v:
            continue
        if U < 0 or U >= u:
            continue
        if T < 0 or T >= t:
            continue
        if S < 0 or S >= s:
            continue
        if R < 0 or R >= r:
            continue
        if Q < 0 or Q >= q:
            continue
        if P < 0 or P >= p:
            continue
        if O < 0 or O >= o:
            continue
        if N < 0 or N >= n:
            continue
        if M < 0 or M >= m:
            continue
        if board[W][V][U][T][S][R][Q][P][O][N][M] == 1:
            continue
        if board[W][V][U][T][S][R][Q][P][O][N][M] == -1:
            continue

        board[W][V][U][T][S][R][Q][P][O][N][M] = 1
        zero_count -= 1

        nxt.append((W, V, U, T, S, R, Q, P, O, N, M))

    if not cur and nxt:
        count += 1
        cur = nxt
        nxt = deque()

if zero_count:
    print(-1)
else:
    print(count)
