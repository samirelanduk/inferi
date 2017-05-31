from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.data import Data
from inferi.exceptions import DuplicateXError

class DataCreationTests(TestCase):

    def test_data_creation_with_values(self):
        data = Data(23, 5, 5)
        self.assertEqual(data._values, [[0, 23], [1, 5], [2, 5]])
        self.assertEqual(data._name, "y")
        self.assertEqual(data._xname, "x")


    def test_data_creation_with_x_values(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data._values, [["K", 23], ["C", 5], ["A", 5]])


    def test_xy_pairs_must_be_len_2(self):
        with self.assertRaises(ValueError):
            Data(("K", 23), ("C", 5), ("A", 5, 6))
        with self.assertRaises(ValueError):
            Data(("K", 23), ("C", 5), ("A",))


    def test_strings_dont_count_as_iterables(self):
        data = Data("Sam", "Jonas", "Sally")
        self.assertEqual(data._values, [[0, "Sam"], [1, "Jonas"], [2, "Sally"]])


    def test_x_values_must_be_unique(self):
        with self.assertRaises(DuplicateXError):
            Data(("K", 23), ("C", 5), ("C", 15))


    def test_can_provide_name(self):
        data = Data(23, 5, 5, name="heights")
        self.assertEqual(data._values, [[0, 23], [1, 5], [2, 5]])
        self.assertEqual(data._name, "heights")
        self.assertEqual(data._xname, "x")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Data(23, 5, 5, name=100)


    def test_can_provide_xname(self):
        data = Data(23, 5, 5, xname="members")
        self.assertEqual(data._values, [[0, 23], [1, 5], [2, 5]])
        self.assertEqual(data._name, "y")
        self.assertEqual(data._xname, "members")


    def test_xname_must_be_str(self):
        with self.assertRaises(TypeError):
            Data(23, 5, 5, xname=100)



class DataReprTests(TestCase):

    def test_repr_no_name(self):
        data = Data(23, 5, 5)
        self.assertEqual(str(data), "<Data (23, 5, 5)>")


    def test_repr_with_name(self):
        data = Data(23, 5, 5, name="IQ")
        self.assertEqual(str(data), "<Data 'IQ' (23, 5, 5)>")



class DataLenTests(TestCase):

    def test_data_len(self):
        data = Data(23, 5, 5)
        self.assertEqual(len(data), 3)



class DataContainerTests(TestCase):

    def test_data_container(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertIn(23, data)
        self.assertNotIn("C", data)



class DataIterableTests(TestCase):

    def test_data_is_iterable(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        for value, correct_value in zip(data, (23, 5, 5)):
            self.assertEqual(value, correct_value)



class DataGetTests(TestCase):

    def test_default_x_get(self):
        data = Data(23, 5, 15)
        self.assertEqual(data[0], 23)
        self.assertEqual(data[1], 5)
        self.assertEqual(data[2], 15)


    def test_custom_x_get(self):
        data = Data(("K", 23), ("C", 5), ("A", 15))
        self.assertEqual(data["K"], 23)
        self.assertEqual(data["C"], 5)
        self.assertEqual(data["A"], 15)


    def test_index_error(self):
        data = Data(23, 5, 15)
        with self.assertRaises(IndexError):
            data[4]



class DataSetTests(TestCase):

    def test_can_create_new_value(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        data["H"] = 17
        self.assertEqual(data._values, [["K", 23], ["C", 5], ["A", 5], ["H", 17]])


    def test_can_update_value(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        data["A"] = 17
        self.assertEqual(data._values, [["K", 23], ["C", 5], ["A", 17]])



class DataDeletionTests(TestCase):

    def test_can_delete_data(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        del data["C"]
        self.assertEqual(data._values, [["K", 23], ["A", 5]])


    def test_deleting_nonexistent_member_is_fine(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        del data["X"]
        self.assertEqual(data._values, [["K", 23], ["C", 5], ["A", 5]])



class DataValuesTests(TestCase):

    def test_can_get_y_values(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.values(), (23, 5, 5))


    def test_can_get_xy_values(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.values(x=True), (("K", 23), ("C", 5), ("A", 5)))



class DataValueAdditionTests(TestCase):

    @patch("inferi.data.Data.xvalues")
    def test_can_add_value(self, mock_x):
        mock_x.return_value = (0, 1, 2)
        data = Data(23, 5, 5)
        data.add(17)
        self.assertEqual(data._values, [[0, 23], [1, 5], [2, 5], [3, 17]])


    @patch("inferi.data.Data.xvalues")
    def test_can_add_value_with_random_x_values(self, mock_x):
        mock_x.return_value = (100, 23, 65)
        data = Data((100, 23), (23, 5), (65, 5))
        data.add(17)
        self.assertEqual(data._values, [[100, 23], [23, 5], [65, 5], [101, 17]])


    @patch("inferi.data.Data.xvalues")
    def test_can_add_value_with_non_int_x_values(self, mock_x):
        mock_x.return_value = (0.1, "F", 0)
        data = Data((0.1, 23), ("F", 5), (0, 5))
        data.add(17)
        self.assertEqual(data._values, [[0.1, 23], ["F", 5], [0, 5], [1, 17]])



class DataNameTests(TestCase):

    def test_can_get_data_name(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), name="a name")
        self.assertIs(data._name, data.name())


    def test_can_update_name(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), name="a name")
        data.name("new name")
        self.assertEqual(data._name, "new name")


    def test_new_name_must_be_str(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), name="a name")
        with self.assertRaises(TypeError):
            data.name(100)



class DataXNameTests(TestCase):

    def test_can_get_data_xname(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), xname="a name")
        self.assertIs(data._xname, data.xname())


    def test_can_update_xname(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), xname="a name")
        data.xname("new name")
        self.assertEqual(data._xname, "new name")


    def test_new_xname_must_be_str(self):
        data = Data(("K", 23), ("C", 5), ("A", 5), xname="a name")
        with self.assertRaises(TypeError):
            data.xname(100)



class DataLengthTests(TestCase):

    @patch("inferi.data.Data.__len__")
    def test_length_is_len(self, mock_len):
        mock_len.return_value = 79
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.length(), 79)



class DataXValuesTests(TestCase):

    def test_can_get_x_values(self):
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.xvalues(), ("K", "C", "A"))



class DataMaxTests(TestCase):

    @patch("inferi.data.Data.values")
    def test_can_get_max(self, mock_values):
        mock_values.return_value = (23, 5, 5)
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.max(), 23)



class DataMinTests(TestCase):

    @patch("inferi.data.Data.values")
    def test_can_get_min(self, mock_values):
        mock_values.return_value = (23, 5, 5)
        data = Data(("K", 23), ("C", 5), ("A", 5))
        self.assertEqual(data.min(), 5)
