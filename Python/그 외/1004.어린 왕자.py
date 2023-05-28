import sys
input = sys.stdin.readline

for _ in range(int(input())):
    count = 0
    st_x, st_y, ed_x, ed_y = map(int, input().split())

    for _ in range(int(input())):
        x, y, r = map(int, input().split())
        is_inside_st = (x-st_x)**2+(y-st_y)**2 <= r**2
        is_inside_ed = (x-ed_x)**2+(y-ed_y)**2 <= r**2

        if is_inside_st ^ is_inside_ed:
            count += 1

    print(count)
