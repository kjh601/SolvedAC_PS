import sys
write = sys.stdout.write

n = int(sys.stdin.readline())
for i in range(n):
    write(' '*i+'*'*(n-i)+'\n')
