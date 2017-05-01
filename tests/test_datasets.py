from unittest import TestCase
from inferi.datasets import Dataset

class DatasetCreationTests(TestCase):

    def test_can_create_empty_dataset(self):
        dataset = Dataset()
        self.assertEqual(dataset._data, {})


    def test_can_create_dataset_with_column_of_data(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertEqual(dataset._data, {0: 23, 1: 5, 2: 5, 3: 18, 4: 17, 5: 20})