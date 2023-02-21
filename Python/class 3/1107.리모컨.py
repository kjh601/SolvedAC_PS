def check(n):
    if n == 0:
        return valid[n]
    while n>0:
        if not valid[n%10]:
            return False
        n//=10
    return True

N = int(input())
M = int(input())

if M:
    broken_button = list(map(int, input().split()))
else :
    broken_button = []
    
valid = [True for _ in range(10)]
for num in broken_button:
    valid[num] = False

count = abs(N-100)
for i in range(1000000):
    if check(i):
        count = min(count, abs(N-i)+len(str(abs(i))))
print(count)