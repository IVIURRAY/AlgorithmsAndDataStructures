class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0:
            return -1

        # choose the fastest way: to move from the head
        # or to move from the tail
        if index < self.size // 2:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.size += 1
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.size += 1

        new_node = Node(val)
        if not self.head:
            self.addAtHead(val)

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            return self.addAtHead(val)

        if index >= self.size or index < 0:
            return

        self.size += 1
        node = self.head
        prev = self.head
        i = 0
        new_node = Node(val)

        # Could also optimise this depending on index
        while i < index:
            prev = node
            node = node.next
            i += 1

        prev.next = new_node
        new_node.next = node
        new_node.prev = prev
        node.prev = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        node = self.head
        prev = self.head
        i = 0
        # Could also optimise this depending on index
        while i < index:
            prev = node
            node = node.next
            i += 1

        prev.next = node.next
        node.next.prev = prev
        self.size -= 1

    def getContents(self):
        head = self.head
        tail = self.tail
        forward = []
        backward = []
        while head:
            forward.append(head.val)
            head = head.next

        while tail:
            backward.append(tail.val)
            tail = tail.prev

        if forward != backward[::-1]:
            raise ValueError(f'The links are broken: Forward {forward} Backwards {backward}')

        return forward


l = DoublyLinkedList()
print('Add at 1 head')  # [1]
l.addAtHead(1)
print(l.getContents())
assert l.getContents() == [1]

print('Add at 3 tail')  # [1, 3]
l.addAtTail(3)
print(l.getContents())
assert l.getContents() == [1, 3]

print('Add 2 at index 1')  # [1, 2, 3]
l.addAtIndex(1, 2)
print(l.getContents())
assert l.getContents() == [1, 2, 3]

print('Get at 1')  # [1, 2, 3]
assert 2 == l.get(1)
print(l.getContents())
assert l.getContents() == [1, 2, 3]

print('Delete at index 1')  # [1, 3]
l.deleteAtIndex(1)
print(l.getContents())
assert l.getContents() == [1, 3]

print('Get at 1')  # [1, 3]
assert 3 == l.get(1)
print(l.getContents())
assert l.getContents() == [1, 3]
