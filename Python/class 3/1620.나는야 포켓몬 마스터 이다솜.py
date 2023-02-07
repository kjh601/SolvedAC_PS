import sys
input = sys.stdin.readline

N, M = map(int,input().split())

pocketmon_dict = dict()
pocketmon_list = list()
for i in range(N):
    name = input().rstrip()
    pocketmon_dict[name] = i
    pocketmon_list.append(name)

for _ in range(M):
    key = input().rstrip()
    if ord(key[0]) < ord('A'):
        print(pocketmon_list[int(key)-1])
    else :
        print(pocketmon_dict[key]+1)
