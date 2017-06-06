from inferi.values import Value
from unittest import TestCase
from unittest.mock import Mock, patch

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



class ValueAdditionTests(TestCase):

    def test_can_add_values(self):
        val1 = Value(23, 0.5)
        val2 = Value(19, 0.4)
        val3 = val1 + val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 42)
        self.assertEqual(val3._error, 0.9)


    def test_can_add_value_to_number(self):
        val1 = Value(23, 0.5)
        val2 = 19.0
        val3 = val1 + val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 42)
        self.assertEqual(val3._error, 0.5)


    def test_can_add_number_to_value(self):
        val1 = 23
        val2 = Value(19, 0.4)
        val3 = val1 + val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 42)
        self.assertEqual(val3._error, 0.4)



class ValueSubtractionTests(TestCase):

    def test_can_subtract_values(self):
        val1 = Value(23, 0.5)
        val2 = Value(19, 0.4)
        val3 = val1 - val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 4)
        self.assertEqual(val3._error, 0.9)


    def test_can_subtract_value_from_number(self):
        val1 = Value(23, 0.5)
        val2 = 19.0
        val3 = val2 - val1
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, -4)
        self.assertEqual(val3._error, 0.5)


    def test_can_subtract_number_from_value(self):
        val1 = 23
        val2 = Value(19, 0.4)
        val3 = val2 - val1
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, -4)
        self.assertEqual(val3._error, 0.4)



class ValueMultiplicationTests(TestCase):

    @patch("inferi.values.Value.relative_error")
    def test_can_multiply_values(self, mock_err):
        mock_err.side_effect = (0.02, 0.03)
        val1 = Value(23, 0.5)
        val2 = Value(19, 0.4)
        val3 = val1 * val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 437)
        self.assertEqual(val3._error, 21.85)


    @patch("inferi.values.Value.relative_error")
    def test_can_multiply_value_with_number(self, mock_err):
        mock_err.return_value = 0.02
        val1 = Value(23, 0.5)
        val2 = 19.0
        val3 = val1 * val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 437)
        self.assertEqual(val3._error, 8.74)


    @patch("inferi.values.Value.relative_error")
    def test_can_multiply_number_with_value(self, mock_err):
        mock_err.return_value = 0.03
        val1 = 23
        val2 = Value(19, 0.4)
        val3 = val1 * val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 437)
        self.assertEqual(val3._error, 13.11)



class ValueDivisionTests(TestCase):

    @patch("inferi.values.Value.relative_error")
    def test_can_divide_values(self, mock_err):
        mock_err.side_effect = (0.02, 0.03)
        val1 = Value(100, 0.5)
        val2 = Value(5, 0.4)
        val3 = val1 / val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 20)
        self.assertEqual(val3._error, 1)


    @patch("inferi.values.Value.relative_error")
    def test_can_divide_value_by_number(self, mock_err):
        mock_err.return_value = 0.02
        val1 = Value(100, 0.5)
        val2 = 5.0
        val3 = val1 / val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 20)
        self.assertEqual(val3._error, 0.4)


    @patch("inferi.values.Value.relative_error")
    def test_can_divide_number_by_value(self, mock_err):
        mock_err.return_value = 0.03
        val1 = 100
        val2 = Value(5, 0.4)
        val3 = val1 / val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 20)
        self.assertEqual(val3._error, 0.6)



class ValuePowerTests(TestCase):

    @patch("inferi.values.Value.relative_error")
    def test_can_raise_value_to_power(self, mock_err):
        mock_err.return_value = 0.01
        val1 = Value(2, 0.02)
        val2 = 3
        val3 = val1 ** val2
        self.assertIsInstance(val3, Value)
        self.assertEqual(val3._value, 8)
        self.assertEqual(val3._error, 0.24)



class ValueEqualityTests(TestCase):

    def test_values_equal(self):
        val1 = Value(19, 0.4)
        val2 = Value(19, 0.5)
        val3 = Value(23, 0.5)
        self.assertEqual(val1, val2)
        self.assertNotEqual(val1, val3)


    def test_value_number_equality(self):
        val1 = Value(19, 0.4)
        val2 = 19.0
        val3 = 23
        self.assertEqual(val1, val2)
        self.assertNotEqual(val1, val3)


    def test_number_value_equality(self):
        val1 = 19
        val2 = Value(19.0, 0.5)
        val3 = Value(23, 0.5)
        self.assertEqual(val1, val2)
        self.assertNotEqual(val1, val3)



class ValueGreaterTests(TestCase):

    def test_value_greater_than_value(self):
        val1 = Value(19, 0.4)
        val2 = Value(23, 0.5)
        self.assertTrue(val2 > val1)
        self.assertTrue(val1 < val2)


    def test_value_greater_than_number(self):
        val1 = 19
        val2 = Value(23, 0.5)
        self.assertTrue(val2 > val1)
        self.assertTrue(val1 < val2)


    def test_number_greater_than_value(self):
        val1 = Value(19, 0.4)
        val2 = 23
        self.assertTrue(val2 > val1)
        self.assertTrue(val1 < val2)



class ValueGreaterEqualTests(TestCase):

    def test_value_greater_equal_than_value(self):
        val1 = Value(19, 0.4)
        val2 = Value(19, 0.5)
        val3 = Value(17, 0.5)
        self.assertTrue(val2 >= val1)
        self.assertTrue(val1 <= val2)
        self.assertTrue(val2 >= val3)


    def test_value_greater_equal_than_number(self):
        val1 = 19
        val2 = Value(19, 0.5)
        self.assertTrue(val2 >= val1)
        self.assertTrue(val1 <= val2)


    def test_number_greater_equal_than_value(self):
        val1 = Value(19, 0.4)
        val2 = 19
        self.assertTrue(val2 >= val1)
        self.assertTrue(val1 <= val2)



class ValueValueTests(TestCase):

    def test_can_get_value(self):
        val = Value(23, 0.5)
        self.assertIs(val.value(), val._value)



class ValueErrorTests(TestCase):

    def test_can_get_error(self):
        val = Value(23, 0.5)
        self.assertIs(val.error(), val._error)



class ValueRelativeErrorTests(TestCase):

    def test_can_get_relative_error(self):
        val = Value(100, 2)
        self.assertEqual(val.relative_error(), 0.02)



class ValueConsistencyTests(TestCase):

    def test_can_get_consistent_results(self):
        val1 = Value(3.3, 0.2)
        val2 = Mock(Value)
        val2.value.return_value = 3.1
        val2.error.return_value = 0.1
        self.assertTrue(val1.consistent_with(val2))


    def test_can_get_inconsistent_results(self):
        val1 = Value(3.30001, 0.2)
        val2 = Mock(Value)
        val2.value.return_value = 3.0
        val2.error.return_value = 0.1
        self.assertFalse(val1.consistent_with(val2))


    def test_can_get_consistency_with_non_value(self):
        val1 = Value(9.87, 0.09)
        val2 = 9.81
        self.assertTrue(val1.consistent_with(val2))
        val2 = 9.78
        self.assertTrue(val1.consistent_with(val2))
        val2 = 9.7799
        self.assertFalse(val1.consistent_with(val2))


    def test_cannot_get_consistency_with_non_number(self):
        val1 = Value(9.87, 0.09)
        with self.assertRaises(TypeError):
            val1.consistent_with("value")
