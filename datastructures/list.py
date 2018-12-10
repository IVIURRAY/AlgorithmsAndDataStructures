"""
Implementation of a list

A node in the list should have a reference to the next node in the list.

Insertion and deletion quick as we just update one node. In arrays we've to shift everything.
Dynamic allocation of memory therefore can grow and shrink without resizing (efficient). But each nodes does store a
pointer to the next node which is quite an overhead.
Indexing nodes is possible but not efficient as we've to traverse all nodes up until we hit our index. Also very
difficult to reverse a linked list in comparision to arrays.
Implement stacks a queues using Lists.
"""


class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


class List(object):

    def __init__(self):
        self.head = None

    def __str__(self):
        values = []  # shhh, kinda cheating
        node = self.head
        while node.next:
            values.append(str(node))
            node = node.next
        return '[{}]'.format(','.join(values + [str(node)]))

    def __repr__(self):
        return 'List %s is %s' % (id(self), self.__str__())

    def append(self, entry):
        """Add a node to the end of the list."""
        if self.head is None:
            self.head = entry
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = entry

    def peak(self):
        """Return the first item in list"""
        return self.head

    def pop(self):
        """Return the first item in list and remove it."""
        if self.head is None:
            node = None
        else:
            node = self.head       # take the head node
            self.head = node.next  # set the start of the list to item 2

        return node

    def print(self):
        """Print the contents of the list"""
        if self.head is None:
            print('List is empty')
        else:
            node = self.head
            while node.next:
                print(node)
                node = node.next
            print(node)


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    print('Initialing the list')
    l = List()
    l.print()

    print('Adding one item')
    l.append(n1)
    l.print()
    print('Adding two items')
    l.append(n2)
    l.print()
    print('Adding three items')
    l.append(n3)
    l.print()
    print(l)
    print('Pop item 1')
    l.pop()
    l.print()
    print('Pop another item')
    l.pop()
    l.print()
    print('Pop again item')
    l.pop()
    l.print()
