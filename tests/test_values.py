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


    def test_can_supply_error(self):
        val = Value(23, 0.03)
        self.assertEqual(val._value, 23)
        self.assertEqual(val._error, 0.03)


    def test_error_requires_numbers(self):
        Value(23, 1)
        Value(23, 0.5)
        with self.assertRaises(TypeError):
            Value(23, "100")
        with self.assertRaises(TypeError):
            Value(23, True)


    def test_error_must_be_positive(self):
        with self.assertRaises(ValueError):
            Value(23, -0.01)



class ValueReprTests(TestCase):

    def test_repr_with_no_error(self):
        val = Value(23)
        self.assertEqual(str(val), '23')


    def test_repr_with_error(self):
        val = Value(23, 0.5)
        self.assertEqual(str(val), '23 ± 0.5')
