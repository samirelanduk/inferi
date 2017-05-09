from unittest import TestCase
from unittest.mock import patch, Mock
from inferi.samples import Sample
from inferi.datasets import Dataset

class SampleCreationTests(TestCase):

    def test_can_create_sample(self):
        sample = Sample(23, 5, 5, 18, 17, 20)
        self.assertEqual(sample._data, {0: 23, 1: 5, 2: 5, 3: 18, 4: 17, 5: 20})


    @patch("inferi.datasets.Dataset.__init__")
    def test_sample_is_dataset(self, mock_init):
        sample = Sample(23, 5, 5, 18, 17, 20)
        mock_init.assert_called
