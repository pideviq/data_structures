from linkedlist.doubly_linked_list import LinkedList


class Stack(LinkedList):
    """Stack implementaition based on deque."""

    name = 'stack'

    def __bool__(self) -> bool:
        for _ in self:
            return True
        else:
            return False

    def push(self, element) -> None:
        """Add element to stack."""
        super().append(element)

    def pop(self):
        """Remove last element and return it's value."""
        if self.tail is None:
            raise IndexError('pop from empty stack')
        popped_element = self.tail
        if self.head == self.tail:
            prev_node = None
            self.head = None
        else:
            prev_node = popped_element.prev
            prev_node.next = None
        self.tail = prev_node
        return popped_element.data
