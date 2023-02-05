N,X = map(int,input().split())
A = map(int,input().split())

nums = list()
for num in A:
    if num<X:
        print(num,end=' ')