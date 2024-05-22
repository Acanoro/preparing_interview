import unittest

from Stack import Stack
from utils import is_balanced


class TestStack(unittest.TestCase):
    def setUp(self):
        """Инициализация стека перед каждым тестом."""
        self.stack = Stack()

    def test_is_empty(self):
        """Тестирование метода is_empty."""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        """Тестирование метода push."""
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_pop(self):
        """Тестирование метода pop."""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        """Тестирование метода peek."""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_size(self):
        """Тестирование метода size."""
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


class TestIsBalanced(unittest.TestCase):
    def test_balanced_sequences(self):
        """Тестирование сбалансированных последовательностей."""
        self.assertEqual(is_balanced("(((([{}]))))"), "Сбалансированно")
        self.assertEqual(is_balanced("[([])((([[[]]])))]{()}"), "Сбалансированно")
        self.assertEqual(is_balanced("{{[()]}}"), "Сбалансированно")
        self.assertEqual(is_balanced(""), "Сбалансированно")

    def test_unbalanced_sequences(self):
        """Тестирование несбалансированных последовательностей."""
        self.assertEqual(is_balanced("}{"), "Несбалансированно")
        self.assertEqual(is_balanced("{{[(])]}}"), "Несбалансированно")
        self.assertEqual(is_balanced("[[{())}]"), "Несбалансированно")
        self.assertEqual(is_balanced("((("), "Несбалансированно")
        self.assertEqual(is_balanced(")))"), "Несбалансированно")
        self.assertEqual(is_balanced("({[)]}"), "Несбалансированно")
        self.assertEqual(is_balanced("(([]))("), "Несбалансированно")

    def test_edge_cases(self):
        """Тестирование крайних случаев."""
        self.assertEqual(is_balanced("()"), "Сбалансированно")
        self.assertEqual(is_balanced("(())"), "Сбалансированно")
        self.assertEqual(is_balanced("([]){}"), "Сбалансированно")
        self.assertEqual(is_balanced("{[()()]}"), "Сбалансированно")
        self.assertEqual(is_balanced("{[(])}"), "Несбалансированно")
