"""hashing"""
n = input()
arr = list(input())
arr = [ord(arr[i])-96 for i in range(len(arr))]
print(sum([arr[i]*31**i for i in range(len(arr))])%1234567891)
