import sys
input = sys.stdin.readline
print = sys.stdout.write


def perfect_number(num):
    arr1 = []
    arr2 = []

    idx = 1
    sqrt_num = int(num**0.5)
    while idx <= sqrt_num:
        if num % idx != 0:
            idx += 1
            continue
        arr1.append(idx)
        arr2.append(num//idx)
        idx += 1
    arr = arr1+list(reversed(arr2))
    total = sum(arr) - num
    if total == num:
        print(str(num)+" = 1")
        for number in arr[1:-1]:
            print(" + "+str(number))
        print('\n')
    else:
        print(str(num)+" is NOT perfect.\n")


while True:
    num = int(input())

    if num == -1:
        break

    perfect_number(num)
