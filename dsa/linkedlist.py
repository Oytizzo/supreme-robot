class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)

    def append(self, data):
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data, self.head.next)
        self.head.next = new_node

    def insert(self, data, new_data):
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass

