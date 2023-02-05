N, K = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = list()

idx = 0
while len(arr)!=0:
    idx = (idx+K-1)%len(arr)
    result.append(str(arr.pop(idx)))
    
print('<'+", ".join(result)+'>')