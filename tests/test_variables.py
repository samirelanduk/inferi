from collections import Counter
from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.variables import Variable, to_value
from inferi.values import Value
from inferi.exceptions import EmptyVariableError

class ValueCreationTests(TestCase):

    def test_can_convert_number_to_value(self):
        val = to_value(100.4)
        self.assertIsInstance(val, Value)
        self.assertEqual(val._value, 100.4)
        self.assertEqual(val._error, 0)


    def test_can_ignore_non_numbers(self):
        s = "100.4"
        val = to_value("100.4")
        self.assertIs(val, s)



class VariableCreationTests(TestCase):

    def test_variable_creation_with_values(self):
        var = Variable(23, 5, 5)
        self.assertEqual(var._values, [23, 5, 5])
        self.assertEqual(var._name, "")


    def test_can_create_variable_from_iterable(self):
        var = Variable([23, 5, 5])
        self.assertEqual(var._values, [23, 5, 5])
        var = Variable((23, 5, 5))
        self.assertEqual(var._values, [23, 5, 5])
        var = Variable(range(100, 103))
        self.assertEqual(var._values, [100, 101, 102])


    def test_strings_dont_count_as_iterables(self):
        var = Variable("A name")
        self.assertEqual(var._values, ["A name"])


    def test_cannot_create_empty_variable(self):
        with self.assertRaises(EmptyVariableError):
            Variable()


    def test_can_provide_name(self):
        var = Variable(23, 5, 5, name="heights")
        self.assertEqual(var._values, [23, 5, 5])
        self.assertEqual(var._name, "heights")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Variable(23, 5, 5, name=100)



class VariableReprTests(TestCase):

    def test_repr_no_name(self):
        var = Variable(23, 5, 5)
        self.assertEqual(str(var), "<Variable (23, 5, 5)>")


    def test_repr_with_name(self):
        var = Variable(23, 5, 5, name="IQ")
        self.assertEqual(str(var), "<Variable 'IQ' (23, 5, 5)>")



class VariableLenTests(TestCase):

    def test_variable_len(self):
        var = Variable(23, 5, 5)
        self.assertEqual(len(var), 3)



class VariableContainerTests(TestCase):

    def test_variable_container(self):
        var = Variable(23, 5, 5)
        self.assertIn(23, var)
        self.assertNotIn(22, var)



class VariableIterableTests(TestCase):

    def test_variable_is_iterable(self):
        var = Variable(23, 5, 6)
        for value, correct_value in zip(var, (23, 5, 6)):
            self.assertEqual(value, correct_value)



class VariableGetTests(TestCase):

    def test_index_lookup(self):
        var = Variable(23, 5, 15)
        self.assertEqual(var[0], 23)
        self.assertEqual(var[1], 5)
        self.assertEqual(var[2], 15)



class VariableSetTests(TestCase):

    def test_can_update_value(self):
        var = Variable(23, 5, 15)
        var[1] = 17
        self.assertEqual(var._values, [23, 17, 15])



class VariableValuesTests(TestCase):

    def test_can_get_values(self):
        var = Variable(23, 5, 15)
        self.assertEqual(var.values(), tuple(var._values))



class VariableValueAdditionTests(TestCase):

    def test_can_add_value(self):
        var = Variable(23, 5, 5)
        var.add(17)
        self.assertEqual(var._values, [23, 5, 5, 17])



class VariableRemovalTests(TestCase):

    def test_can_remove_value(self):
        var = Variable(23, 5, 15)
        var.remove(5)
        self.assertEqual(var._values, [23, 15])


    def test_removing_none_existent_values_is_fine(self):
        var = Variable(23, 5, 15)
        var.remove(6)
        self.assertEqual(var._values, [23, 5, 15])


    def test_cannot_remove_last_value(self):
        var = Variable(23)
        with self.assertRaises(EmptyVariableError):
            var.remove(23)



class VariablePoppingTests(TestCase):

    def test_can_pop_last_value(self):
        var = Variable(23, 5, 15)
        value = var.pop()
        self.assertEqual(var._values, [23, 5])
        self.assertEqual(value, 15)


    def test_can_pop_any_index(self):
        var = Variable(23, 5, 15)
        value = var.pop(1)
        self.assertEqual(var._values, [23, 15])
        self.assertEqual(value, 5)


    def test_cannot_pop_last_value(self):
        var = Variable(23)
        with self.assertRaises(EmptyVariableError):
            var.pop()


    def test_cannot_pop_wrong_index(self):
        var = Variable(23, 5, 15)
        with self.assertRaises(IndexError):
            var.pop(4)


    def test_index_must_be_int(self):
        var = Variable(23, 5, 15)
        with self.assertRaises(TypeError):
            var.pop(0.5)



class VariableNameTests(TestCase):

    def test_can_get_variable_name(self):
        var = Variable(23, 5, 5, name="a name")
        self.assertIs(var._name, var.name())


    def test_can_update_name(self):
        var = Variable(23, 5, 5, name="a name")
        var.name("new name")
        self.assertEqual(var._name, "new name")


    def test_new_name_must_be_str(self):
        var = Variable(23, 5, 5, name="a name")
        with self.assertRaises(TypeError):
            var.name(100)



class VariableLengthTests(TestCase):

    @patch("inferi.variables.Variable.__len__")
    def test_length_is_len(self, mock_len):
        mock_len.return_value = 79
        var = Variable(23, 5, 5, name="a name")
        self.assertEqual(var.length(), 79)



class VariableMaxTests(TestCase):

    @patch("inferi.variables.Variable.values")
    def test_can_get_max(self, mock_values):
        mock_values.return_value = (23, 5, 5)
        var = Variable(23, 5, 5)
        self.assertEqual(var.max(), 23)



class VariableMinTests(TestCase):

    @patch("inferi.variables.Variable.values")
    def test_can_get_min(self, mock_values):
        mock_values.return_value = (23, 5, 5)
        var = Variable(23, 5, 5)
        self.assertEqual(var.min(), 5)



class VariableSumTests(TestCase):

    @patch("inferi.variables.Variable.values")
    def test_variable_sum(self, mock_values):
        mock_values.return_value = (100, 345, 32)
        sample = Variable(100, 345, 32)
        self.assertEqual(sample.sum(), 477)



class VariableMeanTests(TestCase):

    @patch("inferi.variables.Variable.sum")
    @patch("inferi.variables.Variable.length")
    def test_variable_mean(self, mock_length, mock_sum):
        mock_length.return_value = 4
        mock_sum.return_value = 48
        var = Variable(100, 345, 32)
        self.assertEqual(var.mean(), 12)



class VariableMedianTests(TestCase):

    @patch("inferi.variables.Variable.values")
    def test_can_get_odd_median(self, mock_values):
        mock_values.return_value = (100, 345, 32)
        var = Variable(100, 345, 32)
        self.assertEqual(var.median(), 100)


    @patch("inferi.variables.Variable.values")
    def test_can_get_even_median(self, mock_values):
        mock_values.return_value = (20, 30, 40, 50)
        var = Variable(20, 30, 40, 50)
        self.assertEqual(var.median(), 35)



class FrequencyTests(TestCase):

    @patch("inferi.variables.Variable.values")
    def test_can_get_frequencies(self, mock_values):
        mock_values.return_value = (1, 4, 7, 3, 1, 6, 4, 4)
        var = Variable(1, 4, 7, 3, 1, 6, 4, 4)
        self.assertEqual(
         var.frequencies(), Counter({1: 2, 4: 3, 3: 1, 7: 1, 6: 1})
        )



class VariableModeTests(TestCase):

    @patch("inferi.variables.Variable.frequencies")
    def test_can_get_mode(self, mock_frequencies):
        mock_frequencies.return_value = Counter({1: 2, 4: 3, 3: 1, 7: 1, 6: 1})
        var = Variable(1, 1, 1)
        self.assertEqual(var.mode(), 4)


    @patch("inferi.variables.Variable.values")
    def test_no_mode_when_multi_mode(self, mock_values):
        mock_values.return_value = (1, 4, 7, 3, 1, 6, 4)
        var = Variable(1, 4, 7, 3, 1, 6, 4)
        self.assertEqual(var.mode(), None)



class VariableRangeTests(TestCase):

    @patch("inferi.variables.Variable.max")
    @patch("inferi.variables.Variable.min")
    def test_can_get_range(self, mock_min, mock_max):
        mock_max.return_value, mock_min.return_value = 7, 1
        var = Variable(1, 4, 7, 3, 1, 6, 4, 4)
        self.assertEqual(var.range(), 6)



class VariableVarianceTests(TestCase):

    @patch("inferi.variables.Variable.values")
    @patch("inferi.variables.Variable.mean")
    @patch("inferi.variables.Variable.length")
    def test_can_get_variance(self, mock_len, mock_mean, mock_values):
        mock_values.return_value = (600, 470, 170, 430, 300)
        mock_mean.return_value = 394
        mock_len.return_value = 5
        var = Variable(600, 470, 170, 430, 300)
        self.assertEqual(var.variance(), 27130)


    @patch("inferi.variables.Variable.values")
    @patch("inferi.variables.Variable.mean")
    @patch("inferi.variables.Variable.length")
    def test_can_get_population_variance(self, mock_len, mock_mean, mock_values):
        mock_values.return_value = (600, 470, 170, 430, 300)
        mock_mean.return_value = 394
        mock_len.return_value = 5
        var = Variable(600, 470, 170, 430, 300)
        self.assertEqual(var.variance(population=True), 21704)



class VariableStandardDeviationTests(TestCase):

    @patch("inferi.variables.Variable.variance")
    def test_can_get_standard_deviation(self, mock_variance):
        mock_variance.return_value = 25
        var = Variable(600, 470, 170, 430, 300)
        self.assertEqual(var.st_dev(), 5)
        mock_variance.assert_called_with(population=False)


    @patch("inferi.variables.Variable.variance")
    def test_can_get_population_standard_deviation(self, mock_variance):
        mock_variance.return_value = 25
        var = Variable(600, 470, 170, 430, 300)
        self.assertEqual(var.st_dev(population=True), 5)
        mock_variance.assert_called_with(population=True)



class VariableZscoreTests(TestCase):

    @patch("inferi.variables.Variable.mean")
    @patch("inferi.variables.Variable.st_dev")
    def test_can_get_zscore(self, mock_sd, mock_mean):
        var = Variable(600, 470, 170, 430, 300)
        mock_sd.return_value = 300
        mock_mean.return_value = 650
        self.assertEqual(var.zscore(200), -1.5)
        mock_sd.assert_called_with(population=False)


    @patch("inferi.variables.Variable.mean")
    @patch("inferi.variables.Variable.st_dev")
    def test_can_get_population_zscore(self, mock_sd, mock_mean):
        var = Variable(600, 470, 170, 430, 300)
        mock_sd.return_value = 200
        mock_mean.return_value = 650
        self.assertEqual(var.zscore(200, population=True), -2.25)
        mock_sd.assert_called_with(population=True)



class VariableCovarianceTests(TestCase):

    @patch("inferi.variables.Variable.length")
    @patch("inferi.variables.Variable.values")
    @patch("inferi.variables.Variable.mean")
    def test_can_get_covariance(self, mock_mean, mock_values, mock_len):
        mock_mean.return_value = 3.05
        mock_values.return_value = (2.1, 2.5, 4.0, 3.6)
        mock_len.return_value = 4
        var1 = Variable(2.1, 2.5, 4.0, 3.6)
        var2 = Mock(Variable)
        var2.mean.return_value = 11
        var2.values.return_value = (8, 12, 14, 10)
        var2.length.return_value = 4
        self.assertAlmostEqual(var1.covariance_with(var2), 1.53, delta=0.005)


    def test_covariance_requires_variables(self):
        var1 = Variable(2.1, 2.5, 4.0, 3.6)
        with self.assertRaises(TypeError):
            var1.covariance_with("variable")


    @patch("inferi.variables.Variable.length")
    def test_covariance_requires_equal_length_variables(self, mock_length):
        mock_length.return_value = 4
        var1 = Variable(2.1, 2.5, 4.0, 3.6)
        var2 = Mock(Variable)
        var2.length.return_value = 10
        with self.assertRaises(ValueError):
            var1.covariance_with(var2)



class VariableCorrelationTests(TestCase):

    @patch("inferi.variables.Variable.st_dev")
    @patch("inferi.variables.Variable.covariance_with")
    def test_can_get_correlation(self, mock_cov, mock_sd):
        mock_cov.return_value = 42
        mock_sd.return_value = 2
        var1 = Variable(2.1, 2.5, 4.0, 3.6)
        var2 = Mock(Variable)
        var2.st_dev.return_value = 3
        self.assertEqual(var1.correlation_with(var2), 7)
        mock_cov.assert_called_with(var2)
