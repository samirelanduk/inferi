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


    def test_cannot_create_dataset_with_unequal_row_lengths(self):
        with self.assertRaises(ValueError):
            Dataset([3, 45], [5, 43], [2, 21], [4, 55], [1, 34, 4], [3, 34])


    def test_can_supply_x_values(self):
        dataset = Dataset(3, 5, 2, 4, x=["Joe", "Sam", "Guy", "Sue"])
        self.assertEqual(dataset._rows, [[3], [5], [2], [4]])
        self.assertEqual(dataset._x, ["Joe", "Sam", "Guy", "Sue"])
        self.assertEqual(dataset._names, ["y"])
        self.assertEqual(dataset._xname, "x")


    def test_x_must_be_iterable(self):
        with self.assertRaises(TypeError):
            Dataset(3, 5, 2, 4, x=100)


    def test_x_length_must_be_row_length(self):
        with self.assertRaises(ValueError):
            Dataset(3, 5, 2, 4, x=["Joe", "Sam", "Guy"])


    def test_can_supply_name(self):
        dataset = Dataset(3, 5, 2, 4, name="heights")
        self.assertEqual(dataset._rows, [[3], [5], [2], [4]])
        self.assertEqual(dataset._x, [0, 1, 2, 3])
        self.assertEqual(dataset._names, ["heights"])
        self.assertEqual(dataset._xname, "x")


    def test_can_supply_name_to_multiple_columns(self):
        dataset = Dataset([3, 45], [5, 43], [2, 21], [4, 55], name="heights")
        self.assertEqual(
         dataset._rows, [[3, 45], [5, 43], [2, 21], [4, 55]]
        )
        self.assertEqual(dataset._x, [0, 1, 2, 3])
        self.assertEqual(dataset._names, ["heights", "heights2"])
        self.assertEqual(dataset._xname, "x")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Dataset(3, 5, 2, 4, name=100)


    def test_can_supply_names(self):
        dataset = Dataset([3, 45], [5, 43], [2, 21], names=["heights", "weights"])
        self.assertEqual(
         dataset._rows, [[3, 45], [5, 43], [2, 21]]
        )
        self.assertEqual(dataset._x, [0, 1, 2])
        self.assertEqual(dataset._names, ["heights", "weights"])
        self.assertEqual(dataset._xname, "x")


    def test_names_must_be_str(self):
        with self.assertRaises(TypeError):
            Dataset([3, 45], [5, 43], [2, 21], names=["heights", 100, "weights"])


    def test_names_must_be_same_width_as_dataset(self):
        with self.assertRaises(ValueError):
            Dataset([3, 45], [5, 43], [2, 21], names=["heights", "100", "weights"])


    def test_names_take_precedence_over_name(self):
        dataset = Dataset([3, 45], [5, 43], [2, 21], name="zzz", names=["heights", "weights"])
        self.assertEqual(
         dataset._rows, [[3, 45], [5, 43], [2, 21]]
        )
        self.assertEqual(dataset._x, [0, 1, 2])
        self.assertEqual(dataset._names, ["heights", "weights"])
        self.assertEqual(dataset._xname, "x")


    def test_can_supply_x_name(self):
        dataset = Dataset(3, 5, 2, 4, 1, 3, x_name="inputs")
        self.assertEqual(dataset._rows, [[3], [5], [2], [4], [1], [3]])
        self.assertEqual(dataset._x, [0, 1, 2, 3, 4, 5])
        self.assertEqual(dataset._names, ["y"])
        self.assertEqual(dataset._xname, "inputs")


    def test_x_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Dataset(3, 5, 2, 4, 1, 3, x_name=100)
