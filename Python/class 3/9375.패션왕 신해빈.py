import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cloth_type_count = dict()

    for _ in range(N):
        cloth_name, cloth_type = input().sjrstrip().split()
        if cloth_type in cloth_type_count:
            cloth_type_count[cloth_type] += 1
        else :
            cloth_type_count[cloth_type] = 1

    count = 1
    for cloth_type in cloth_type_count.keys():
        count *= cloth_type_count[cloth_type]+1
    print(count - 1)
