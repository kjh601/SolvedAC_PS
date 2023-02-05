string = input()
loc = [-1 for i in range(26)]
string_len = len(string)

for i in range(string_len):
    if loc[ord(string[i])-ord('a')]==-1:
        loc[ord(string[i])-ord('a')] = i

for i in loc:
    print(i,end=' ')