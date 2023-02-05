"""벌집"""
N = int(input())
count = 1
while N>3*count**2-3*count+1:
    count+=1
print(count)
