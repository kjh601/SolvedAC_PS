import sys
input = sys.stdin.readline
write = sys.stdout.write
while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break

    write(str(M+F)+'\n')
