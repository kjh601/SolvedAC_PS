import sys
write = sys.stdout.write

N = int(input())
for i in range(1, N+1):
    write(' '*(N-i)+'*'*(1+(i-1)*2)+'\n')
