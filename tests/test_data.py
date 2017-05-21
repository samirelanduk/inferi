from unittest import TestCase
from inferi.data import Data

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
