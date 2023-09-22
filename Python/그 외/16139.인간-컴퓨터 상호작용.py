import sys

input = sys.stdin.readline
write = sys.stdout.write

string = ' '+input().rstrip()
length = len(string)
counts = [[0]*26]

for i in range(1, length):
    tmp = counts[i-1][:]
    tmp[ord(string[i])-97] += 1
    counts.append(tmp)

q = int(input())
for _ in range(q):
    char, l, r = input().split()
    idx = ord(char)-97
    write(str(counts[int(r)+1][idx]-counts[int(l)][idx])+'\n')
