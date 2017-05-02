from unittest import TestCase
from inferi import Series

class SeriesTests(TestCase):

    def test_series_handling(self):
        series = Series(4, 8, 15, 16, 23, 42)
        self.assertEqual(series.length(), 6)
        self.assertEqual(series.data(), (4, 8, 15, 16, 23, 42))

        series.add(108)
        self.assertEqual(series.length(), 7)
        self.assertEqual(series.data(), (4, 8, 15, 16, 23, 42, 108))

        series.remove(23)
        series.remove(8)
        self.assertEqual(series.length(), 5)
        self.assertEqual(series.data(), (4, 15, 16, 23, 108))
