import linkedlist.singly_linked_list


class Node(linkedlist.singly_linked_list.Node):
    """Doubly Linked List element."""

    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None


class LinkedList(linkedlist.singly_linked_list.LinkedList):
    """Doubly Linked List data structure."""

    name = 'doubly_linked_list'

    def __init__(self, items=None) -> None:
        self.head = None
        self.tail = None
        if items is not None:
            node = Node(items.pop(0))
            self.head = self.tail = node
            for item in items:
                node.next = Node(item)
                node.prev, node = node, node.next
                self.tail = node

    def append(self, item) -> None:
        """Append new node to the end of list."""
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev, self.tail = self.tail, new_node

    def prepend(self, item) -> None:
        """Prepend list with new node."""
        new_node = Node(item)
        first_node = self.head
        self.head = new_node
        if first_node is None:
            self.tail = new_node
        else:
            new_node.next = first_node
            first_node.prev = new_node

    def insert(self, item, after_node_data):
        """Insert new node after node with specified data."""
        if self.head is None:
            raise IndexError('List is empty')
        for node in self:
            if node.data == after_node_data:
                new_node = Node(item)
                new_node.prev = node
                new_node.next = node.next
                node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                return
        raise ValueError(f'Node with data {after_node_data} not found')

    def remove(self, node_data):
        """Remove node with specified data from list."""
        if self.head is None:
            raise IndexError('List is empty')
        prev_node = None
        for node in self:
            if node.data == node_data and type(node.data) == type(node_data):
                if prev_node is None:
                    # Removing first element
                    self.head = node.next
                    self.head.prev = None
                else:
                    next_node = node.next
                    prev_node.next = next_node
                    if next_node is None:
                        # Removing last element
                        self.tail = prev_node
                    else:
                        next_node.prev = prev_node
                return
            prev_node = node
        raise ValueError(f'Node with data {node_data} not found')
