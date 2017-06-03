from inferi.values import Value
from unittest import TestCase

class ValueCreationTests(TestCase):

    def test_can_create_value(self):
        val = Value(23)
        self.assertEqual(val._value, 23)
        self.assertEqual(val._error, 0)


    def test_value_requires_numbers(self):
        Value(23)
        Value(23.5)
        with self.assertRaises(TypeError):
            Value("100")
        with self.assertRaises(TypeError):
            Value(True)
