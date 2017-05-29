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
