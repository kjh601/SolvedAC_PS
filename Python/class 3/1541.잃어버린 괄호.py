arr = input()

idx = 0
length = len(arr)
while idx < length and arr[idx] != '-': idx+=1
result=sum(list(map(int,arr[:idx].split('+'))))
if idx < length:
    result-=sum(map(int,arr[idx:].replace('-',' ').replace('+',' ').split()))
print(result)
