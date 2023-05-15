import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
preorder = [None for _ in range(n)]
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def recursion(Pst, Ped, Ist, Ied, idx, len):
    root = postorder[Ped]
    preorder[idx] = root
    leftNodeCount = 0
    while leftNodeCount < len-1 and inorder[Ist+leftNodeCount] != root:
        leftNodeCount += 1
    rightNodeCount = len-leftNodeCount-1
    if leftNodeCount > 0:
        recursion(Pst, Pst+leftNodeCount-1, Ist, Ist +
                  leftNodeCount-1, idx+1, leftNodeCount)
    if rightNodeCount > 0:
        recursion(Pst+leftNodeCount, Ped-1, Ist+leftNodeCount +
                  1, Ied, idx+leftNodeCount+1, rightNodeCount)


recursion(0, n-1, 0, n-1, 0, n)
print(' '.join(map(str, preorder)))
