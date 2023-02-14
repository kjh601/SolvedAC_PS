N, r, c = map(int,input().split())
length = 2**N
result = 0
start_r = 0
end_r = length
start_c = 0
end_c = length
while True :
    mid_r = (start_r+end_r)//2
    mid_c = (start_c+end_c)//2
    length//=2
    if length==0:
        break
    if r<mid_r and c<mid_c:
        result += (length)**2*0
        end_r = mid_r
        end_c = mid_c
    elif r<mid_r and c>=mid_c:
        result += (length)**2*1
        end_r = mid_r
        start_c = mid_c
    elif r>=mid_r and c<mid_c:
        result += (length)**2*2
        start_r = mid_r
        end_c = mid_c
    elif r>=mid_r and c>=mid_c:
        result += (length)**2*3
        start_r = mid_r
        start_c = mid_c
print(result)