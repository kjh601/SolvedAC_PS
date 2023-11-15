import sys
input = sys.stdin.readline

N = int(input())
mapping_dict = {
    '0': 0,
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31,
    'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
    'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
    'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}


def findParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_all_connect():
    tmp = findParent(parent, parent[0])
    for node in parent[1:]:
        if tmp != findParent(parent, node):
            return False
    return True


matrix = [input().rstrip() for _ in range(N)]
edge = sorted([(i, j, mapping_dict[matrix[i][j]])
              for i in range(N) for j in range(N) if matrix[i][j] != '0'], key=lambda x: x[2])

parent = [i for i in range(N)]


total = sum(x[2] for x in edge)
for v1, v2, w in edge:
    if findParent(parent, v1) == findParent(parent, v2):
        continue
    unionParent(parent, v1, v2)
    total -= w

if is_all_connect():
    print(total)
else:
    print(-1)
