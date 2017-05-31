from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.samples import Sample
from inferi.data import Data

class SampleCreationTests(TestCase):

    @patch("inferi.data.Data.__init__")
    def test_can_create_sample(self, mock_init):
        mock_init.return_value = None
        sample = Sample(100, 345, 32)
        self.assertIsInstance(sample, Data)
        mock_init.assert_called_with(100, 345, 32)



class SampleReprTests(TestCase):

    def test_repr_no_name(self):
        sample = Sample(100, 345, 32)
        self.assertEqual(str(sample), "<Sample (100, 345, 32)>")


    def test_repr_with_name(self):
        sample = Sample(100, 345, 32, name="numbers")
        self.assertEqual(str(sample), "<Sample 'numbers' (100, 345, 32)>")



class SampleSumTests(TestCase):

    def test_sample_sum(self):
        sample = Sample(100, 345, 32)
        self.assertEqual(sample.sum(), 477)



class SampleMeanTests(TestCase):

    @patch("inferi.samples.Sample.sum")
    @patch("inferi.samples.Sample.length")
    def test_sample_mean(self, mock_length, mock_sum):
        mock_length.return_value = 4
        mock_sum.return_value = 48
        sample = Sample(100, 345, 32)
        self.assertEqual(sample.mean(), 12)



class SampleMedianTests(TestCase):

    @patch("inferi.samples.Sample.values")
    def test_can_get_odd_median(self, mock_values):
        mock_values.return_value = (100, 345, 32)
        sample = Sample(100, 345, 32)
        self.assertEqual(sample.median(), 100)


    @patch("inferi.samples.Sample.values")
    def test_can_get_even_median(self, mock_values):
        mock_values.return_value = (20, 30, 40, 50)
        sample = Sample(20, 30, 40, 50)
        self.assertEqual(sample.median(), 35)



class ModeTests(TestCase):

    @patch("inferi.samples.Sample.values")
    def test_can_get_mode(self, mock_values):
        mock_values.return_value = (1, 4, 7, 3, 1, 6, 4, 4)
        sample = Sample(1, 4, 7, 3, 1, 6, 4, 4)
        self.assertEqual(sample.mode(), 4)


    @patch("inferi.samples.Sample.values")
    def test_no_mode_when_multi_mode(self, mock_values):
        mock_values.return_value = (1, 4, 7, 3, 1, 6, 4)
        sample = Sample(1, 4, 7, 3, 1, 6, 4)
        self.assertEqual(sample.mode(), None)
