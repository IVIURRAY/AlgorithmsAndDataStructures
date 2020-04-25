class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.result = []

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        new_node = Node(value)
        while node.val is not None:
            if value > node.val:
                if not node.right:
                    node.right = new_node
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = new_node
                    break
                else:
                    node = node.left


def pre_order_recursion(root):
    result = []

    if root:
        result.append(root)
        result = result + pre_order_recursion(root.left)
        result = result + pre_order_recursion(root.right)

    return result


def in_order_recursion(root):
    result = []
    if root:
        result = in_order_recursion(root.left)
        result.append(root.val)
        result = result + in_order_recursion(root.right)

    return result


def post_order_recursion(root):
    result = []

    if root:
        result = post_order_recursion(root.left)
        result = result + post_order_recursion(root.right)
        result.append(root)

    return result


def pre_order_iterative(root):
    stack = []
    result =  []
    node = root

    while stack or node:
        if node:
            result.append(node)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right

    return result


def in_order_iterative(root):
    stack = []
    result = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node)
            node = node.right

    return result


def post_order_iterative(root):
    stack = []
    result = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            result = [node] + result
            node = node.right
        else:
            node = stack.pop()
            node = node.left

    return result


bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

'''
        20
       /   \
     9      25
   /  \
  5    12
      /   \
     11   14
'''
print(f'PreOrder    - Recursion: {pre_order_recursion(bst.root)}')
print(f'InOrder     - Recursion: {in_order_recursion(bst.root)}')
print(f'PostOrder   - Recursion: {post_order_recursion(bst.root)}')

print(f'PreOrder    - Iterative: {pre_order_iterative(bst.root)}')
print(f'InOrder     - Iterative: {in_order_iterative(bst.root)}')
print(f'PostOrder   - Iterative: {post_order_iterative(bst.root)}')
