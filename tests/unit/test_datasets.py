from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.variables import Variable
from inferi.datasets import Dataset

class DatasetTest(TestCase):

    def setUp(self):
        self.variables = [Mock(Variable), Mock(Variable), Mock(Variable)]



class DatasetCreationTests(DatasetTest):

    def test_can_create_datasets(self):
        dataset = Dataset(*self.variables)
        self.assertEqual(dataset._variables, self.variables)


    def test_dataset_needs_variables(self):
        with self.assertRaises(TypeError):
            Dataset(self.variables[0], "list")



class DatasetReprTests(DatasetTest):

    def test_dataset_repr(self):
        dataset = Dataset(*self.variables)
        self.assertEqual(str(dataset), "<Dataset (3 Variables)>")
