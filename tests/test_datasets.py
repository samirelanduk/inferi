from unittest import TestCase
from inferi.datasets import Dataset

class DatasetCreationTests(TestCase):

    def test_can_create_empty_dataset(self):
        dataset = Dataset()
        self.assertEqual(dataset._data, {})


    def test_can_create_dataset_with_column_of_data(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertEqual(dataset._data, {0: 23, 1: 5, 2: 5, 3: 18, 4: 17, 5: 20})



class DatasetReprTests(TestCase):

    def test_dataset_repr(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertEqual(str(dataset), "<Dataset (23, 5, 5, 18, 17, 20)>")



class DatasetLenTests(TestCase):

    def test_dataset_len(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertEqual(len(dataset), 6)



class DatasetContainerTests(TestCase):

    def test_dataset_container(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertIn(23, dataset)
        self.assertIn(5, dataset)
        self.assertNotIn(1, dataset)



class DatasetIterableTests(TestCase):

    def test_can_iterate_through_dataset(self):
        dataset, members = Dataset(23, 5, 5, 18, 17, 20), []
        for value in dataset:
            members.append(value)
        self.assertEqual(members, [23, 5, 5, 18, 17, 20])



class DatasetIndexingTests(TestCase):

    def test_can_get_values_by_index(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        for index, value in enumerate([23, 5, 5, 18, 17, 20]):
            self.assertEqual(dataset[index], value)



class DatasetValueSettingTests(TestCase):

    def test_can_set_values(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        dataset[0] = 22
        self.assertEqual(dataset._data, {0: 22, 1: 5, 2: 5, 3: 18, 4: 17, 5: 20})
        dataset[7] = 1
        self.assertEqual(dataset._data, {0: 22, 1: 5, 2: 5, 3: 18, 4: 17, 5: 20, 7: 1})



class DatasetLengthTests(TestCase):

    def test_length_is_len(self):
        dataset = Dataset(23, 5, 5, 18, 17, 20)
        self.assertEqual(dataset.length(), len(dataset))
