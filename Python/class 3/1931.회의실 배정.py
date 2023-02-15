import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    st, ed = map(int,input().split())
    meetings.append((ed,st))

ed = 0
count = 0
for meeting in sorted(meetings):
    if meeting[1] < ed:
        continue
    ed = meeting[0]
    count+=1

print(count)
