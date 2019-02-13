"""
Binary tree representation
"""

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other


n1 = Node(10)
n2 = Node(5)
n3 = Node(20)
n4 = Node(9)
n5 = Node(18)
n6 = Node(3)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

"""
Level, Nodes
1:          10
          /     \
2:      5        20
      /   \     /   \
3:  9      18  3     7
"""


def visit(node):
    if node:
        print(node.data)


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        visit(root)
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root is not None:
        visit(root)
        in_order_traversal(root.left)
        in_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        in_order_traversal(root.right)
        visit(root)


print('In order:')
in_order_traversal(n1)
print('Pre order')
pre_order_traversal(n1)
print('Post order')
post_order_traversal(n1)


def dfs_simple(root):
    if root is None:
        return

    visit(root)
    if root.left:
        dfs_simple(root.left)
    if root.right:
        dfs_simple(root.right)


def dfs_depth_of_target_at_first_occurrence(root, target):
    if root is None:
        return 0

    if root == target:
        return 1

    left_dfs = dfs_depth_of_target_at_first_occurrence(root.left, target)
    right_dfs = dfs_depth_of_target_at_first_occurrence(root.right, target)

    depth = max(left_dfs, right_dfs)
    return depth + 1 if depth else depth


print('dfs')
dfs_simple(n1)
print('dfs with target')
print(dfs_depth_of_target_at_first_occurrence(n1, 10))
print(dfs_depth_of_target_at_first_occurrence(n1, 5))
print(dfs_depth_of_target_at_first_occurrence(n1, 18))
print(dfs_depth_of_target_at_first_occurrence(n1, 3))


def bfs_simple(root):
    q = [root]
    while q:
        n = q.pop(0)
        visit(n)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

def bfs_is_target_in(root, target):
    q = [root]
    while q:
        n = q.pop(0)
        if n == target:
            return True
        visit(n)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

    return False


def bfs_is_target_in_return_node(root, target):
    q = [root]
    while q:
        n = q.pop(0)
        if n == target:
            return n
        visit(n)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

    return Node()

print('bfs')
bfs_simple(n1)
print('bfs with target')
print(bfs_is_target_in(n1, 101))
print(bfs_is_target_in(n1, 5))

def route_between_two_nodes(root, a, b):
    if a == b:
        return True
    q = [root]

    while q:
        n = q.pop(0)
        if n == a:
            a_children = [n]
            while a_children:
                child = a_children.pop(0)
                if child == b:
                    return True
                if child.left is not None:
                    a_children.append(child.left)
                if child.right is not None:
                    a_children.append(child.right)

        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

    return False


def route_between_two_nodes2(root, a, b):
    a_tree = bfs_is_target_in_return_node(root, a)
    if a_tree:
        return bfs_is_target_in(a_tree, b)

    return False


print('Route between two nodes')
print(route_between_two_nodes(n1, Node(5), Node(18)))
print(route_between_two_nodes2(n1, Node(5), Node(18)))
