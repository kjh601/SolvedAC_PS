import sys
N = int(sys.stdin.readline())
arr = list(tuple(map(int,sys.stdin.readline().split())) for _ in range(N))
for x,y in sorted(arr, key=lambda x:(x[1],x[0])):
    sys.stdout.write(str(x)+' '+str(y)+'\n')