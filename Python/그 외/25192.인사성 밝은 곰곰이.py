import sys
input = sys.stdin.readline

N = int(input())
gomgom = set()
count = 0
for _ in range(N):
    string = input().rstrip()
    if string == "ENTER":
        count += len(gomgom)
        gomgom = set()
    else:
        gomgom.add(string)
count += len(gomgom)
print(count)
