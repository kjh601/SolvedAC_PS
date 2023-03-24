import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value)

root = None
for line in sys.stdin:
    value = int(line)
    if root is None:
        root = Node(value)
    else:
        node = root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    break
                node = node.right

postorder(root)