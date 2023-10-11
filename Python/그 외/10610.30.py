arr = sorted(input(), reverse=True)

if arr[-1] != '0' or sum(map(int, arr)) % 3 != 0:
    print(-1)
else:
    print(''.join(arr))
