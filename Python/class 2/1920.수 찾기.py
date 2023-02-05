'''
바이너리 함수 구현
O(logn)
'''
import sys

def binary_search(num, arr):
    length = len(A)
    front = 0
    rear = length
    while front!=rear:
        mid = (front+rear)//2
        if num==arr[mid]:
            return '1'
        elif num<arr[mid]:
            rear = mid
        else :
            front = mid+1
    return '0'
    

N = int(sys.stdin.readline())
A = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
for num in map(int,sys.stdin.readline().split()):
    sys.stdout.write(binary_search(num,A)+'\n')


'''
자료형 세트와 in연산자
세트는 기본적으로 데이타를 해쉬값으로 저장해서
시간복잡도가 O(n)이고 충돌이 많은 경우에 O(n)이 된다.
'''

N = sys.stdin.readline()
A = set(sys.stdin.readline().split())
M = sys.stdin.readline()
B = sys.stdin.readline().split()

for num in B:
    if num in A:
        sys.stdout.write('1\n')
    else :
        sys.stdout.write('0\n')