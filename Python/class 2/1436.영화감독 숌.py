def check_666(num):
    count = 0
    while num>0:
        if num%10 == 6:
            count += 1
        else :
            count = 0
        if count == 3:
            return True
        num//=10
    return False

N = int(input())
num = 665
for i in range(N):
    while True:
        num+=1
        if check_666(num):
            result = num
            break
print(result)