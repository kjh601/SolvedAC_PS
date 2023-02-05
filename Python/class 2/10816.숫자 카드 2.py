import sys
input = sys.stdin.readline

cards = dict()

N = int(input())
for num in list(map(int,input().split())):
    if num in cards:
        cards[num]+=1
    else :
        cards[num]=1

M = int(input())
for ans in list(map(int,input().split())):
    if ans in cards:
        print(cards[ans],end=' ')
    else :
        print(0,end=' ')