N, L = map(int, input().split())
sum = 0
for i in range(1, 101):
    sum += i
    if i==100 or sum > N:
        print(-1)
        break
    if i+1 >= L and not (N-sum)%(i+1):
        for j in range(i+1):
            print((N-sum)//(i+1)+j, end=' ')
        break