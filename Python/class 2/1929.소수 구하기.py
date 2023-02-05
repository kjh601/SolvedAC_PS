M,N = map(int, input().split())

prime_nums = [2]
if M<=2:
    print(2)
for num in range(3,N+1,2):
    flag = True
    for prime_num in prime_nums:
        if prime_num>int(num**(1/2)):
            break
        if num%prime_num==0:
            flag = False
            break
    if flag:
        prime_nums.append(num)
        if num >= M:
            print(num)
        
        