import unittest
from stack.stack import Stack


class TestStack(unittest.TestCase):
    """Test Stack implementation."""

    def setUp(self) -> None:
        self.values = [
            101,
            'abc',
        ]
        self.repr_template = 'stack([{}])'

    def test_push(self):
        """Test add element to stack."""
        stack = Stack()
        self.assertFalse(stack)
        stack.push(self.values[0])
        self.assertTrue(stack)
        self.assertEqual(repr(stack),
                         self.repr_template.format(self.values[0]))
        stack.push(self.values[1])
        values_repr = ', '.join(str(value) for value in self.values)
        self.assertEqual(repr(stack),
                         self.repr_template.format(values_repr))

    def test_pop(self):
        """Test remove last element from stack."""
        stack = Stack()
        with self.subTest(msg='Remove from empty stack', stack=stack):
            with self.assertRaises(IndexError):
                stack.pop()
        for el in self.values:
            stack.push(el)
        with self.subTest(msg='Remove last element', stack=stack, el=el):
            self.assertEqual(stack.pop(), el)
        with self.subTest(msg='Remove the only element', stack=stack):
            stack.pop()
            self.assertIsNone(stack.tail)
            self.assertIsNone(stack.head)
            self.assertFalse(stack)


if __name__ == 'main':
    unittest.main()
