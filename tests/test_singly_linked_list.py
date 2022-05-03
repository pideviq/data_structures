import unittest
from linkedlist.singly_linked_list import LinkedList, Node


class TestSinglyLinkedList(unittest.TestCase):
    """Test Singly Linked List implementation."""

    def setUp(self) -> None:
        self.typed_items = {
            'int': 23,
            'float': 3.14,
            'int_str': '45',
            'str': 'abc',
            'bool': True,
            'none': None,
        }
        self.items_dict = {
            'first': 101,
            'second': 'abc',
            'insert_after_first': '45d',
        }

    def test_single_node(self):
        """Test Node implementation."""
        for name, value in self.typed_items.items():
            node = Node(value)
            with self.subTest(node=node, name=name, value=value):
                self.assertEqual(node.data, value)
                self.assertIsNone(node.next)
                self.assertTrue(repr(node) == str(value))

    def test_linked_list_init_empty(self):
        """Test new Linked List initialization with no data."""
        empty_list = LinkedList()
        self.assertIsNone(empty_list.head)

    def test_linked_list_init_with_items(self):
        """Test new Linked List initialization with data."""
        items = list(self.typed_items.values())
        linked_list = LinkedList(items[:])
        # Check first element
        with self.subTest(
                msg='Check first element', linked_list=linked_list,
                items=items):
            self.assertEqual(linked_list.head.data, items[0])
            second_node = linked_list.head.next
            self.assertEqual(second_node.data, items[1])
        # Iterate over the list and check all elements' data
        for node, expected_data in zip(linked_list, self.typed_items.values()):
            with self.subTest(
                    msg="Check all elements' data", node=node,
                    expected_data=expected_data):
                self.assertEqual(node.data, expected_data)
        # Check last element
        with self.subTest(msg='Check last element reference', node=node):
            self.assertIsNone(node.next)

    def test_append(self):
        """Test appending new nodes to the end of Linked List."""
        linked_list = LinkedList()
        first_node = None
        with self.subTest(
                msg='Test append to empty list', linked_list=linked_list):
            linked_list.append(self.items_dict['first'])
            first_node = linked_list.head
            self.assertIsNotNone(first_node)
            self.assertEqual(first_node.data, self.items_dict['first'])
            self.assertIsNone(first_node.next)
        with self.subTest(
                msg='Test append to non-empty list', linked_list=linked_list,
                first_node=first_node):
            linked_list.append(self.items_dict['second'])
            second_node = first_node.next
            self.assertIsNotNone(second_node)
            self.assertEqual(second_node.data, self.items_dict['second'])
            self.assertIsNone(second_node.next)

    def test_prepend(self):
        """Test prepending Linked List with new node."""
        linked_list = LinkedList()
        first_node = None
        with self.subTest(
                msg='Test prepend empty list', linked_list=linked_list):
            linked_list.prepend(self.items_dict['first'])
            first_node = linked_list.head
            self.assertIsNotNone(first_node)
            self.assertEqual(first_node.data, self.items_dict['first'])
            self.assertIsNone(first_node.next)
        with self.subTest(
                msg='Test prepend non-empty list',
                linked_list=linked_list):
            linked_list.prepend(self.items_dict['second'])
            first_node = linked_list.head
            second_node = first_node.next
            self.assertIsNotNone(first_node)
            self.assertIsNotNone(second_node)
            self.assertEqual(first_node.data, self.items_dict['second'])
            self.assertEqual(first_node.next, second_node)
            self.assertEqual(second_node.data, self.items_dict['first'])
            self.assertIsNone(second_node.next)

    def test_insert(self):
        """Test inserting element after the node."""
        linked_list = LinkedList()
        # Test handling insert to empty list
        with self.subTest(
                msg='Test insert in empty list', linked_list=linked_list):
            with self.assertRaises(IndexError):
                linked_list.insert(self.items_dict['insert_after_first'], self.items_dict['first'])
        linked_list.append(self.items_dict['first'])
        linked_list.append(self.items_dict['second'])
        # Test proper insertion
        linked_list.insert(self.items_dict['insert_after_first'], self.items_dict['first'])
        first_node = linked_list.head
        self.assertEqual(first_node.data, self.items_dict['first'])
        second_node = first_node.next
        self.assertIsNotNone(second_node.next)
        self.assertEqual(second_node.data, self.items_dict['insert_after_first'])
        third_node = second_node.next
        self.assertEqual(third_node.data, self.items_dict['second'])
        self.assertIsNone(third_node.next)
        # Test handling insert after incorrect element
        with self.subTest(
                msg='Test insert after incorrect element',
                linked_list=linked_list):
            with self.assertRaises(ValueError):
                linked_list.insert(False, 'incorrect value')

    def test_clean(self):
        """Test cleaning Linked List."""
        items = list(self.typed_items.values())
        linked_list = LinkedList(items[:])
        linked_list.clean()
        self.assertIsNone(linked_list.head)

    def test_linked_list_repr(self):
        """Test Linked List representation."""
        items = list(self.typed_items.values())
        linked_list = LinkedList(items[:])
        string_repr = 'singly_linked_list(['\
                      + ', '.join(str(item) for item in items)\
                      + '])'
        self.assertEqual(repr(linked_list), string_repr)

    def test_remove(self):
        """Test removing element from Linked List."""
        items = [1, 'abc', True, '45d', None]
        empty_list = LinkedList()
        # Test handling remove from empty list
        with self.subTest(
                msg='Test remove from empty list', empty_list=empty_list):
            with self.assertRaises(IndexError):
                empty_list.remove(items[0])
        # Test proper removing
        linked_list = LinkedList(items[:])
        first_node = linked_list.head
        second_node = first_node.next
        third_node = second_node.next
        fourth_node = third_node.next
        last_node = fourth_node.next
        with self.subTest(
                msg='Test remove from the middle', linked_list=linked_list):
            linked_list.remove(third_node.data)
            new_third_node = second_node.next
            # Third node becomes old fourth
            self.assertEqual(new_third_node.data, fourth_node.data)
            self.assertEqual(new_third_node.next, fourth_node.next)
        with self.subTest(msg='Test remove first', linked_list=linked_list):
            linked_list.remove(first_node.data)
            new_first_node = linked_list.head
            self.assertEqual(new_first_node.data, 'abc')
            self.assertEqual(new_first_node.next, second_node.next)
        with self.subTest(msg='Test remove last', linked_list=linked_list):
            linked_list.remove(last_node.data)
            # Get last node
            for node in linked_list:
                pass
            self.assertEqual(node.data, '45d')
            self.assertIsNone(node.next)
        # Test handling remove incorrect element
        with self.subTest(
                msg='Test remove incorrect element',
                linked_list=linked_list):
            with self.assertRaises(ValueError):
                linked_list.remove('incorrect value')


if __name__ == 'main':
    unittest.main()
