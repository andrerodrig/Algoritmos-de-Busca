class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '<%s - %s>' % (
            self.__class__.__name__,
            self.value
        )

class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def append(self, node: Node):
        if self.head:
            temp = self.head
            self.head = Node(node)
            self.head.next = temp
        else:
            self.head = Node(node)
        return self.head

    def add_final(self, node: Node):
        if not self.head:
            self.head = Node(node)
            return self.head
        return add_final(self.head.next)

