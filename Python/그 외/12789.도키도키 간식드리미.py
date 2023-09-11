N = int(input())
arr1 = list(reversed(list(map(int, input().split()))))
arr2 = []

idx = 1
while True:
    if arr1 and arr1[-1] == idx:
        arr1.pop()
        idx += 1
    elif arr2 and arr2[-1] == idx:
        arr2.pop()
        idx += 1
    elif arr1:
        arr2.append(arr1.pop())
    elif arr2:
        print("Sad")
        break
    else:
        print("Nice")
        break
