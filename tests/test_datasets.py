from unittest import TestCase
from inferi.datasets import Dataset

class DatasetCreationTests(TestCase):

    def test_can_create_dataset_with_list_of_values(self):
        dataset = Dataset(3, 5, 2, 4, 1, 3)
        self.assertEqual(dataset._rows, [[3], [5], [2], [4], [1], [3]])
        self.assertEqual(dataset._x, [0, 1, 2, 3, 4, 5])
        self.assertEqual(dataset._names, ["y"])
        self.assertEqual(dataset._xname, "x")


    def test_can_create_dataset_with_multiple_columns(self):
        dataset = Dataset([3, 45], [5, 43], [2, 21], [4, 55], [1, 34], [3, 34])
        self.assertEqual(
         dataset._rows, [[3, 45], [5, 43], [2, 21], [4, 55], [1, 34], [3, 34]]
        )
        self.assertEqual(dataset._x, [0, 1, 2, 3, 4, 5])
        self.assertEqual(dataset._names, ["y", "y2"])
        self.assertEqual(dataset._xname, "x")
