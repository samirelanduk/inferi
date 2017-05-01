from unittest import TestCase
from inferi.datasets import Dataset

class DatasetCreationTests(TestCase):

    def test_can_create_empty_dataset(self):
        dataset = Dataset()
        self.assertEqual(dataset._data, {})
