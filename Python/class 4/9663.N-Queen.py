count = 0
arr = []


def backtracking(x):
    global count
    if x == N:
        count += 1
        return
    for y in range(N):
        flag = False
        for i, j in enumerate(arr):
            if y == j or x-i == y-j or -x+i == y-j:
                flag = True
                break
        if flag:
            continue
        arr.append(y)
        backtracking(x+1)
        arr.pop()


N = int(input())
backtracking(0)
print(count)
