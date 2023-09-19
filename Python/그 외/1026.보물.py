A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()

sum = 0
for i in range(int(input())):
    sum += B[i]*A[i]

print(sum)
