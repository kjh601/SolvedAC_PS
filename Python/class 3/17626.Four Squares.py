N = int(input())
square_nums = []
dp = [5]*50001
for i in range(1,N+1):
    #본인이 제곱수
    if i**0.5%1 == 0:
        dp[i] = 1
        square_nums.append(i)
        #본인이 제곱수가 아닐 경우
    else :
        for square_num in reversed(square_nums):
            if dp[i] == 2:
                break
            if square_num<i/4:
                break
            dp[i] = min(dp[i],dp[square_num]+dp[i-square_num])

print(dp[N])