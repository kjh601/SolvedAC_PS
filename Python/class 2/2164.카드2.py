import math

N = int(input())
if N==1:
    print(1)
else:
    print((N-2**int(math.log2(N-1)))*2)