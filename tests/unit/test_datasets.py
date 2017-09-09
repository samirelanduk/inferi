from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.variables import Variable
from inferi.datasets import Dataset

class DatasetTest(TestCase):

    def setUp(self):
        self.variables = [Mock(Variable), Mock(Variable), Mock(Variable)]
        for var in self.variables:
            var.length.return_value = 4



class DatasetCreationTests(DatasetTest):

    def test_can_create_datasets(self):
        dataset = Dataset(*self.variables)
        self.assertEqual(dataset._variables, self.variables)


    def test_dataset_needs_variables(self):
        with self.assertRaises(TypeError):
            Dataset(self.variables[0], "list")


    def test_dataset_variables_must_be_equal_length(self):
        self.variables[0].length.return_value = 3
        with self.assertRaises(ValueError):
            Dataset(*self.variables)



class DatasetReprTests(DatasetTest):

    def test_dataset_repr(self):
        dataset = Dataset(*self.variables)
        self.assertEqual(str(dataset), "<Dataset (3 Variables)>")



class DatasetIndexingTests(DatasetTest):

    def test_dataset_index(self):
        dataset = Dataset(*self.variables)
        self.assertIs(dataset[0], self.variables[0])
        self.assertIs(dataset[1], self.variables[1])
        self.assertIs(dataset[2], self.variables[2])



class DatasetVariablesTests(DatasetTest):

    def test_can_get_variables(self):
        dataset = Dataset(*self.variables)
        self.assertEqual(dataset.variables(), tuple(self.variables))



class DatasetVariableAdditionTests(DatasetTest):

    def test_can_add_variable(self):
        dataset = Dataset(self.variables[0])
        dataset.add_variable(self.variables[1])
        self.assertEqual(dataset._variables, self.variables[:2])
        dataset.add_variable(self.variables[2])
        self.assertEqual(dataset._variables, self.variables)


    def test_can_add_first_variable(self):
        dataset = Dataset()
        dataset.add_variable(self.variables[0])
        self.assertEqual(dataset._variables, [self.variables[0]])


    def test_can_only_add_variables(self):
        dataset = Dataset(self.variables[0])
        with self.assertRaises(TypeError):
            dataset.add_variable("var")


    def test_can_only_add_variables_of_correct_length(self):
        dataset = Dataset(self.variables[0])
        self.variables[1].length.return_value = 3
        with self.assertRaises(ValueError):
            dataset.add_variable(self.variables[1])



class DatasetVariableInsertionTests(DatasetTest):

    def test_can_insert_variable(self):
        dataset = Dataset(*self.variables[0:2])
        dataset.insert_variable(1, self.variables[2])
        self.assertEqual(
         dataset._variables,
         [self.variables[0], self.variables[2], self.variables[1]]
        )


    def test_can_insert_first_variable(self):
        dataset = Dataset()
        dataset.insert_variable(0, self.variables[0])
        self.assertEqual(dataset._variables, [self.variables[0]])


    def test_can_only_insert_variables(self):
        dataset = Dataset(self.variables[0])
        with self.assertRaises(TypeError):
            dataset.insert_variable(0, "var")


    def test_can_only_insert_variables_of_correct_length(self):
        dataset = Dataset(self.variables[0])
        self.variables[1].length.return_value = 3
        with self.assertRaises(ValueError):
            dataset.insert_variable(0, self.variables[1])



class DatasetRemovalTests(DatasetTest):

    def test_can_remove_variable(self):
        dataset = Dataset(*self.variables[0:2])
        dataset.remove_variable(self.variables[0])
        self.assertEqual(dataset._variables, [self.variables[1]])



class DatasetPoppingTests(DatasetTest):

    def test_can_pop_last_variable(self):
        dataset = Dataset(*self.variables)
        variable = dataset.pop_variable()
        self.assertEqual(dataset._variables, self.variables[:2])
        self.assertEqual(variable, self.variables[-1])


    def test_can_pop_any_index(self):
        dataset = Dataset(*self.variables)
        variable = dataset.pop_variable(0)
        self.assertEqual(dataset._variables, self.variables[1:])
        self.assertEqual(variable, self.variables[0])


    def test_cannot_pop_wrong_index(self):
        dataset = Dataset(*self.variables)
        with self.assertRaises(IndexError):
            dataset.pop_variable(4)


    def test_index_must_be_int(self):
        dataset = Dataset(*self.variables)
        with self.assertRaises(TypeError):
            dataset.pop_variable(0.5)
