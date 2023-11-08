input()

s3 = sorted(list(set(map(int, input().split())).difference(
    set(map(int, input().split())))))
length = len(s3)
print(length)
if length:
    print(' '.join(map(str, s3)))
