N = int(input())

arr = list(map(int, input().split()))

scores = [0] * (1000001)
card_exits = [False] * (1000001)

for num in arr:
    card_exits[num] = True

for i in range(N):
    for j in range(arr[i] * 2, 1000001, arr[i]):
        if card_exits[j]:
            scores[arr[i]] += 1
            scores[j] -= 1

for i in range(N):
    print(scores[arr[i]], end=" ")
