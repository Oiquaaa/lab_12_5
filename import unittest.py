import unittest
from laba5 import Stack, evaluate

class TestEvaluate(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_evaluate_expression(self):
        a, b, c, d = 1, 2, 3, 4
        expression = 'abcda + cd - a //*-+'
        result = evaluate(expression, a, b, c, d)       
        self.assertEqual(result, 18.0)


if __name__ == '__main__':
    unittest.main(exit=False)
