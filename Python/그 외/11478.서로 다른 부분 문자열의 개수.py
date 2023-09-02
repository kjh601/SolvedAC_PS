S = input().rstrip()
length = len(S)
arr = set()

for i in range(length):
    for j in range(i, length):
        arr.add(S[i:j+1])

print(len(arr))
