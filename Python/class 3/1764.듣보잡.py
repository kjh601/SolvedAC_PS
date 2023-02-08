import sys
input = sys.stdin.readline

N,M = map(int,input().split())
no_listen = set([input().rstrip() for _ in range(N)])
no_watch = set([input().rstrip() for _ in range(M)])

names = sorted(list(no_listen & no_watch))
print(len(names))
for name in names:
    print(name)