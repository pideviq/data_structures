class Node:
    """Linked List element."""
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    """Linked List data structure."""

    def __init__(self, items=None) -> None:
        self.head = None
        if items is not None:
            node = Node(items.pop(0))
            self.head = node
            for item in items:
                node.next = Node(item)
                node = node.next
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes_data = []
        for node in self:
            nodes_data.append(str(node.data))
        return 'singly_linked_list([' + ', '.join(nodes_data) + '])'

    def append(self, item) -> None:
        """Append new node to the end of list."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            for node in self:
                pass
            node.next = new_node

    def prepend(self, item) -> None:
        """Prepend list with new node."""
        new_node = Node(item)
        first_node = self.head
        self.head = new_node
        if first_node is not None:
            new_node.next = first_node

    def insert(self, item, after_node_data):
        """Insert new node after node with specified data."""
        if self.head is None:
            raise IndexError('List is empty')
        for node in self:
            if node.data == after_node_data:
                new_node = Node(item)
                node.next, new_node.next = new_node, node.next
                return
        raise ValueError(f'Node with data {after_node_data} not found')

    def clean(self):
        """Clean list."""
        self.__init__()

    def remove(self, node_data):
        """Remove node with specified data from list."""
        if self.head is None:
            raise IndexError('List is empty')
        prev_node = None
        for node in self:
            if node.data == node_data and type(node.data) == type(node_data):
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
        raise ValueError(f'Node with data {node_data} not found')
