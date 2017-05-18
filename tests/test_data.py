from unittest import TestCase
from inferi.data import Data

class DataCreationTests(TestCase):

    def test_data_creation_with_values(self):
        data = Data(23, 5, 5, 18, 17, 20)
        self.assertEqual(
         data._values,
         [[0, 23], [1, 5], [2, 5], [3, 18], [4, 17], [5, 20]]
        )
