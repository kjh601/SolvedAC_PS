import sys
input = sys.stdin.readline
print = sys.stdout.write


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node: Node):
    print(node.data)
    if node.left_node:
        pre_order(tree[node.left_node])
    if node.right_node:
        pre_order(tree[node.right_node])


def in_order(node: Node):
    if node.left_node:
        in_order(tree[node.left_node])
    print(node.data)
    if node.right_node:
        in_order(tree[node.right_node])


def post_order(node: Node):
    if node.left_node:
        post_order(tree[node.left_node])
    if node.right_node:
        post_order(tree[node.right_node])
    print(node.data)


N = int(input())
tree = dict()

for _ in range(N):
    parent, left, right = input().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[parent] = Node(parent, left, right)
pre_order(tree['A'])
print('\n')
in_order(tree['A'])
print('\n')
post_order(tree['A'])
