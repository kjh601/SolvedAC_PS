"""수 정렬하기 2"""
N = int(input())
arr = [int(input()) for i in range(N)]

arr.sort()

print('\n'.join(map(str, arr)))
