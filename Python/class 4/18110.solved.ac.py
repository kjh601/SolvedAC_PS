import sys
inp = sys.stdin.readline


def r(x):
    return int(x) + (x - int(x) >= 0.5)


n = int(inp())
d = sorted(int(inp()) for _ in range(n))

t = r(n * 0.15) if n != 0 else 0
t = int(t)
td = d[t:-t or None]
ad = r(sum(td) / len(td)) if n != 0 else 0
print(int(ad))
