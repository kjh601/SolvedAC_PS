N, a, b = map(int,input().split())

def nextNum(num):
    return (num+1)//2

count = 0
while True:
    count += 1
    a = nextNum(a)
    b = nextNum(b)
    if a == b:
        print(count)
        break