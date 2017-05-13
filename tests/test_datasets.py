from unittest import TestCase
from inferi.datasets import Dataset

class DatasetCreationTests(TestCase):

    def test_can_create_dataset_with_list_of_values(self):
        dataset = Dataset(3, 5, 2, 4, 1, 3)
        self.assertEqual(dataset._rows, [[3], [5], [2], [4], [1], [3]])
        self.assertEqual(dataset._x, [0, 1, 2, 3, 4, 5])
        self.assertEqual(dataset._names, ["y1"])
        self.assertEqual(dataset._xname, "x")
