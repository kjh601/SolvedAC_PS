N = int(input())
M = int(input())
string = input().rstrip()
count = 0
result = 0
idx = 0
while idx < M:
    if string[idx] == 'I':
        while True:
            idx += 2
            if idx >= M or string[idx-1] != 'O' or string[idx] != 'I':
                idx -= 1
                result += max(0,count-N+1)
                count = 0
                break
            count += 1
    else :
        idx += 1

print(result)